// Custom MathJax loader - typeset math after page load
window.addEventListener('load', function() {
    if (window.MathJax) {
        MathJax.typesetPromise().catch(function(err) {
            console.log('MathJax typeset failed:', err);
        });
    }
});
