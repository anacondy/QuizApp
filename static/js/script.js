document.addEventListener('DOMContentLoaded', () => {
    // --- ELEMENT REFERENCES ---
    const quizTitleElement = document.getElementById('quiz-title');
    const questionText = document.getElementById('question-text');
    const optionsContainer = document.querySelector('.options-container');
    const questionCounterElement = document.getElementById('question-counter');
    const paginationContainer = document.getElementById('pagination-container');
    const sectionNameElement = document.getElementById('section-name');
    const finishPromptElement = document.getElementById('finish-prompt');
    const themeToggleBtn = document.getElementById('theme-toggle');
    const categoryNav = document.getElementById('category-nav');
    const toastContainer = document.getElementById('toast-container');

    // --- STATE MANAGEMENT ---
    let questions = [];
    let currentQuestionIndex = 0;
    let userAnswers = [];
    let currentTheme = localStorage.getItem('quizTheme') || 'matrix';

    // --- INITIALIZATION ---
    document.body.className = `theme-${currentTheme}`;
    themeToggleBtn.textContent = currentTheme === 'matrix' ? '✨' : '💻';
    const urlParams = new URLSearchParams(window.location.search);
    const category = urlParams.get('category');
    if (!category) { questionText.textContent = "Error: No category selected."; showToast("Error: No category selected!", "error"); return; }
    document.title = `${category} Practice Quiz`;
    quizTitleElement.textContent = `${category} Quiz`;
    document.addEventListener('keydown', handleKeyDown);
    fetchQuestions(category);

    // --- EVENT LISTENERS ---
    themeToggleBtn.addEventListener('click', toggleTheme);
    categoryNav.addEventListener('click', handleCategoryChange);

    function fetchQuestions(selectedCategory) {
        fetch(`/api/questions?category=${selectedCategory}`).then(response => response.json()).then(data => {
            if (data.error) { questionText.textContent = `Error: ${data.error}`; showToast(`Error: ${data.error}`, "error"); return; }
            questions = data;
            userAnswers = Array(questions.length).fill(null);
            createPagination();
            navigateToQuestion(0);
            if (sessionStorage.getItem('categorySwitch')) { showToast(`Switched to ${selectedCategory} Quiz!`); sessionStorage.removeItem('categorySwitch'); }
        }).catch(error => { console.error("Error fetching questions:", error); questionText.textContent = "Failed to load questions."; showToast("Failed to load questions.", "error"); });
    }

    function navigateToQuestion(index) {
        if (index < 0 || index >= questions.length || questions.length === 0) { return; }
        currentQuestionIndex = index;
        const questionData = questions[currentQuestionIndex];
        sectionNameElement.textContent = questionData.section;
        questionText.textContent = questionData.question;
        optionsContainer.innerHTML = '';
        questionData.options.forEach((option, i) => {
            const button = document.createElement('button');
            button.textContent = `${String.fromCharCode(65 + i)}. ${option}`;
            button.addEventListener('click', () => selectAnswer(option));
            optionsContainer.appendChild(button);
        });
        updatePagination();
        updateCounter();
        restoreAnswerState();
    }

    // --- REWRITTEN CORE LOGIC ---
    function selectAnswer(selectedOption) {
    userAnswers[currentQuestionIndex] = selectedOption;
    updateCounter();
    updatePagination();

    // ➤➤➤ NEW: Add visual magic effect to selected button
    const optionButtons = optionsContainer.querySelectorAll('button');
    optionButtons.forEach(btn => {
        const optionText = btn.textContent.substring(3); // Remove "A. ", "B. " prefix
        if (optionText === selectedOption) {
            btn.classList.add('option-selected');
        } else {
            btn.classList.remove('option-selected'); // Ensure only one has it
        }
        btn.disabled = true; // Still disable all after selection
    });

    const allAnswered = userAnswers.every(answer => answer !== null);

    if (allAnswered) {
        checkCompletion(); // Shows "Press ENTER" prompt
    } else if (currentQuestionIndex < questions.length - 1) {
        setTimeout(() => {
            navigateToQuestion(currentQuestionIndex + 1);
        }, 180); // ⚡ Faster transition!
    }
}


    function finishQuiz() {
        let finalScore = 0;
        userAnswers.forEach((answer, index) => {
            if (answer && answer === questions[index].answer) { finalScore++; }
        });
        const reviewData = questions.map((q, index) => ({
            question: q.question, userAnswer: userAnswers[index], correctAnswer: q.answer, isCorrect: userAnswers[index] === q.answer
        }));
        sessionStorage.setItem('quizResults', JSON.stringify({
        score: finalScore,
        totalQuestions: questions.length,
        review: reviewData // ← This contains: question, userAnswer, correctAnswer, isCorrect
        }));
        window.location.href = '/results';
    }

    // --- UI UPDATE & HELPER FUNCTIONS ---
    function checkCompletion() {
    const allAnswered = userAnswers.every(answer => answer !== null);
    if (allAnswered) {
        finishPromptElement.textContent = "✅ All questions answered! Press ENTER to see results.";
        finishPromptElement.classList.add('visible');
        // Optional: Add a gentle pulse animation for attention
        finishPromptElement.style.animation = 'pulse 1.5s infinite';
    } else {
        finishPromptElement.classList.remove('visible');
        finishPromptElement.style.animation = 'none';
    }
}

    function updateCounter() {
        const answeredCount = userAnswers.filter(a => a !== null).length;
        questionCounterElement.textContent = `Answered: ${answeredCount} / ${questions.length}`;
    }

    function createPagination() {
        paginationContainer.innerHTML = '';
        for (let i = 0; i < questions.length; i++) {
            const btn = document.createElement('button');
            btn.className = 'pagination-btn';
            btn.textContent = i + 1;
            btn.addEventListener('click', () => navigateToQuestion(i));
            paginationContainer.appendChild(btn);
        }
    }

    function updatePagination() {
        const buttons = paginationContainer.querySelectorAll('.pagination-btn');
        buttons.forEach((btn, index) => {
            btn.classList.remove('active', 'answered');
            if (index === currentQuestionIndex) {
                btn.classList.add('active');
                btn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
            }
            if (userAnswers[index] !== null) {
                btn.classList.add('answered');
            }
        });
    }

    function restoreAnswerState() {
    const userAnswer = userAnswers[currentQuestionIndex];
    const optionButtons = optionsContainer.querySelectorAll('button');

    optionButtons.forEach((btn, i) => {
        const optionText = btn.textContent.substring(3); // "A. Option" → "Option"

        if (userAnswer) {
            btn.disabled = true;

            // ➤➤➤ Preserve selection marker, but remove correctness colors
            if (optionText === userAnswer) {
                btn.classList.add('option-selected');
            } else {
                btn.classList.remove('option-selected');
            }

            // Ensure no premature right/wrong coloring
            btn.classList.remove('correct', 'incorrect');
        } else {
            btn.disabled = false;
            btn.classList.remove('option-selected', 'correct', 'incorrect');
        }
    });
}



    function handleKeyDown(e) {
    // Always prevent default for quiz navigation keys
    if (['ArrowLeft', 'ArrowRight', 'Enter'].includes(e.key)) {
        e.preventDefault();
    }

    switch (e.key) {
        case 'ArrowLeft': case '<':
            navigateToQuestion((currentQuestionIndex - 1 + questions.length) % questions.length);
            break;
        case 'ArrowRight': case '>':
            navigateToQuestion((currentQuestionIndex + 1) % questions.length);
            break;
        case 'Enter':
            if (userAnswers.every(answer => answer !== null)) {
                finishQuiz(); // This will redirect to /results
            } else if (currentQuestionIndex < questions.length - 1) {
                navigateToQuestion(currentQuestionIndex + 1);
            }
            // Optional: Show toast if trying to press Enter before finishing
            else {
                showToast("Answer all questions first!", "error", 1500);
            }
            break;
        case 'a': case 'A': paginationContainer.scrollLeft -= 60; break;
        case 'd': case 'D': paginationContainer.scrollLeft += 60; break;
    }
}


    function toggleTheme() {
        currentTheme = document.body.classList.contains('theme-matrix') ? 'glass' : 'matrix';
        document.body.className = `theme-${currentTheme}`;
        localStorage.setItem('quizTheme', currentTheme);
        themeToggleBtn.textContent = currentTheme === 'matrix' ? '✨' : '💻';
    }

    function handleCategoryChange(event) {
        if (event.target.tagName === 'A') {
            event.preventDefault();
            const newCategory = new URLSearchParams(event.target.href.split('?')[1]).get('category');
            if (newCategory && newCategory !== category) {
                sessionStorage.setItem('categorySwitch', 'true');
                setTimeout(() => { window.location.href = event.target.href; }, 300);
            }
        }
    }

    function showToast(message, type = "success", duration = 2000) {
        const toast = document.createElement('div');
        toast.className = `toast-popup ${type}`;
        toast.textContent = message;
        toastContainer.appendChild(toast);
        setTimeout(() => toast.classList.add('show'), 10);
        setTimeout(() => { toast.classList.remove('show'); toast.addEventListener('transitionend', () => toast.remove()); }, duration);
    }
});