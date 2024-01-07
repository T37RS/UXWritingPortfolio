document.addEventListener("DOMContentLoaded", function () {
    const startButton = document.getElementById("start-button");
    const features = document.querySelectorAll(".feature");

    startButton.addEventListener("click", function () {
        features.forEach((feature, index) => {
            setTimeout(() => {
                feature.classList.add("active");
            }, index * 500);
        });
    });
});