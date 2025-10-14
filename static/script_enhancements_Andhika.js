document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // NAVBAR SCROLL EFFECT
    // ============================================
    const navDhika = document.querySelector('.navDhika');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navDhika.classList.add('scrolled-dhika');
        } else {
            navDhika.classList.remove('scrolled-dhika');
        }
    });
    
    // ============================================
    // FORM INPUT ANIMATIONS
    // ============================================
    const inputsDhika = document.querySelectorAll('.inputDhika input, .inputDhika select, .form-control');
    
    inputsDhika.forEach(input => {
        // Add filled class when input has value
        if (input.value) {
            input.classList.add('filled-dhika');
        }
        
        input.addEventListener('blur', function() {
            if (this.value) {
                this.classList.add('filled-dhika');
            } else {
                this.classList.remove('filled-dhika');
            }
        });
    });
    
    // ============================================
    // PASSWORD TOGGLE
    // ============================================
    const toggleDhika = document.querySelector('.toggle-Dhika');
    if (toggleDhika) {
        toggleDhika.addEventListener('click', function() {
            const inputDhika = this.previousElementSibling;
            if (inputDhika.type === 'password') {
                inputDhika.type = 'text';
                this.innerHTML = '<i class="fas fa-eye-slash"></i>';
            } else {
                inputDhika.type = 'password';
                this.innerHTML = '<i class="fas fa-eye"></i>';
            }
        });
    }
    
    // ============================================
    // RIPPLE EFFECT FOR BUTTONS
    // ============================================
    const buttonsDhika = document.querySelectorAll('.btn, .nav-link-dhika');
    
    buttonsDhika.forEach(button => {
        button.addEventListener('click', function(e) {
            const rippleDhika = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            rippleDhika.style.width = rippleDhika.style.height = size + 'px';
            rippleDhika.style.left = x + 'px';
            rippleDhika.style.top = y + 'px';
            rippleDhika.classList.add('ripple-effect-dhika');
            
            this.appendChild(rippleDhika);
            
            setTimeout(() => rippleDhika.remove(), 600);
        });
    });
    
    // ============================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ============================================
    const anchorLinksDhika = document.querySelectorAll('a[href^="#"]');
    
    anchorLinksDhika.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '') {
                e.preventDefault();
                const targetDhika = document.querySelector(href);
                if (targetDhika) {
                    targetDhika.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // ============================================
    // TABLE RESPONSIVE DATA LABELS
    // ============================================
    const tablesDhika = document.querySelectorAll('.tableDhika');
    
    tablesDhika.forEach(table => {
        const headersDhika = Array.from(table.querySelectorAll('th')).map(th => th.textContent);
        const cellsDhika = table.querySelectorAll('tbody td');
        
        cellsDhika.forEach((cell, index) => {
            const headerIndex = index % headersDhika.length;
            cell.setAttribute('data-label', headersDhika[headerIndex]);
        });
    });
    
    // ============================================
    // FORM VALIDATION ENHANCEMENT
    // ============================================
    const formsDhika = document.querySelectorAll('.inputDhika');
    
    formsDhika.forEach(form => {
        const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
        
        inputs.forEach(input => {
            input.addEventListener('invalid', function(e) {
                e.preventDefault();
                this.classList.add('error-dhika');
            });
            
            input.addEventListener('input', function() {
                if (this.validity.valid) {
                    this.classList.remove('error-dhika');
                    this.classList.add('valid-dhika');
                }
            });
        });
    });
    
    // ============================================
    // ANIMATION ON SCROLL (Optional)
    // ============================================
    const observerDhika = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible-dhika');
            }
        });
    }, {
        threshold: 0.1
    });
    
    const animatedElementsDhika = document.querySelectorAll('.form-group, .info-box, .instructions, .tableDhika, .card-dhika');
    animatedElementsDhika.forEach(el => observerDhika.observe(el));
    
    // ============================================
    // NUMBER INPUT INCREMENT/DECREMENT
    // ============================================
    const numberInputsDhika = document.querySelectorAll('input[type="number"]');
    
    numberInputsDhika.forEach(input => {
        // Add increment/decrement on mouse wheel
        input.addEventListener('wheel', function(e) {
            if (document.activeElement === this) {
                e.preventDefault();
                const step = parseFloat(this.step) || 1;
                const current = parseFloat(this.value) || 0;
                
                if (e.deltaY < 0) {
                    this.value = current + step;
                } else {
                    this.value = current - step;
                }
                
                this.dispatchEvent(new Event('input', { bubbles: true }));
            }
        });
    });
    
    // ============================================
    // AUTO-RESIZE TEXTAREA
    // ============================================
    const textareasDhika = document.querySelectorAll('textarea');
    
    textareasDhika.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });
    
    console.log('✨ Dhika Enhancements Loaded Successfully!');
});

// CSS untuk ripple effect (tambahkan ke style_Andhika.css)
const rippleStyleDhika = `
.ripple-effect-dhika {
    position: absolute;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.6);
    transform: scale(0);
    animation: ripple-animation-dhika 0.6s ease-out;
    pointer-events: none;
}

@keyframes ripple-animation-dhika {
    to {
        transform: scale(4);
        opacity: 0;
    }
}

.error-dhika {
    border-color: var(--error-dhika) !important;
    animation: shake-dhika 0.3s ease;
}

.valid-dhika {
    border-color: var(--success-dhika) !important;
}

@keyframes shake-dhika {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
}

.visible-dhika {
    animation: fadeInUpDhika 0.6s ease-out;
}
`;