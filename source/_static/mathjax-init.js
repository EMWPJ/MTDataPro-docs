// Custom MathJax loader for myst_parser output
window.addEventListener('load', function() {
    // Configure MathJax
    window.MathJax = {
        options: {
            enableMenu: false,
            processHtmlClass: "math",
        },
        tex2jax: {
            inlineMath: [['$', '$'], ['\\(', '\\)']],
            displayMath: [['$$', '$$'], ['\\[', '\\]']],
            processEscapes: true,
        },
        startup: {
            pageReady: function() {
                return MathJax.startup.defaultPageReady();
            }
        }
    };
    
    // Load MathJax
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/mathjax@4/esm/tex-mml-chtml.js';
    script.async = true;
    document.head.appendChild(script);
});
