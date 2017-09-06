/**
 * @author eduardo22i / http://estampworld.com/
*/

var upper_slider;
var timer;

//General Functions

function codeAddress() {
    upper_slider = document.getElementById("upper_slider");
}

function fullScreen () {
    var dif = (window.innerWidth / parseInt(document.getElementById("upper_slider").style.width) );
    document.getElementById("upper_slider").style.width = "auto";
    document.getElementById("upper_slider").style.height = "200px";
    
    var firstIMG = document.getElementById("upper_slider").getElementsByTagName('img')[0];
    firstIMG.width =  "100%";
    firstIMG.height = "100%";
    
    window.addEventListener("resize", fullScreen);

    console.log(document.getElementById("upper_slider").style.height);
}

function KSTransitionTimer(imgNext) {
        // clearInterval(timer);

        upper_slider.innerHTML = "";
        upper_slider.style.width = "auto";
        upper_slider.style.height = "200px";

        var imagePart = document.createElement('img');
        upper_slider.appendChild(imagePart);
        imagePart.setAttribute('width', '100%');
        imagePart.setAttribute('height', '100%');

        imagePart.src = imgNext;
 }

//Effects 

function KSDissolve ( image, imgNext, nextLink) {
    
    codeAddress();
    upper_slider.innerHTML = "";
    upper_slider.style.width = "auto";
    upper_slider.style.height = "200px";

    var iDiv = document.createElement('div');
    iDiv.className = 'dissolve';
    iDiv.style.width = "auto";
    iDiv.style.height = "200px";
    upper_slider.appendChild(iDiv);

    var imagePart = document.createElement('img');
    imagePart.src = image;
    imagePart.setAttribute('width', '100%');
    imagePart.setAttribute('height', '100%');
    iDiv.appendChild(imagePart);

    upper_slider.style.background = "url(" + imgNext + ")";
    upper_slider.style.backgroundSize = "cover";
    upper_slider.style.backgroundOrigin = "center";
    upper_slider.setAttribute('data-url', nextLink);

    // timer = setInterval(function () {KSTransitionTimer(imgNext)}, 100);
    KSTransitionTimer(imgNext);
} 

function KSSlideUp ( image, imgNext, nextLink) {
    
    codeAddress();
    upper_slider.innerHTML = "";
    upper_slider.style.width = "auto";
    upper_slider.style.height = "200px";
    
    var iDiv = document.createElement('div');
    iDiv.className = 'slideUp';
    iDiv.style.width = "auto";
    iDiv.style.height = "200px";
    upper_slider.appendChild(iDiv);

    var imagePart = document.createElement('img');
    imagePart.src = image;
    imagePart.width = "100%";
    imagePart.height = "100%";
    iDiv.appendChild(imagePart);
    
    upper_slider.style.background = "url(" + imgNext + ")";
    upper_slider.style.backgroundSize = "cover";
    upper_slider.setAttribute('data-url', nextLink);

    // timer = setInterval(function () {KSTransitionTimer(imgNext)}, 100);
    KSTransitionTimer(imgNext);
} 

function KSSlideDown ( image, imgNext, nextLink) {
    
    codeAddress();
    upper_slider.innerHTML = "";
    upper_slider.style.width = "auto";
    upper_slider.style.height = "200px";
    
    var iDiv = document.createElement('div');
    iDiv.className = 'slideDown';
    iDiv.style.width = "auto";
    iDiv.style.height = "200px";
    upper_slider.appendChild(iDiv);

    var imagePart = document.createElement('img');
    imagePart.src = image;
    imagePart.setAttribute('width', '100%');
    imagePart.setAttribute('height', '100%');
    iDiv.appendChild(imagePart);

    upper_slider.style.background = "url(" + imgNext + ")";
    upper_slider.style.backgroundSize = "cover";
    upper_slider.setAttribute('data-url', nextLink);

    // timer = setInterval(function () {KSTransitionTimer(imgNext)}, 100);
    KSTransitionTimer(imgNext);
} 

function KSSlideLeft ( image, imgNext, nextLink) {
    
    codeAddress();
    upper_slider.innerHTML = "";
    upper_slider.style.width = "auto";
    upper_slider.style.height = "200px";

    var iDiv = document.createElement('div');
    iDiv.className = 'slideLeft';
    iDiv.style.width = "auto";
    iDiv.style.height = "200px";
    upper_slider.appendChild(iDiv);

    var imagePart = document.createElement('img');
    imagePart.src = image;
    imagePart.width = "100%";
    imagePart.height = "100%";
    iDiv.appendChild(imagePart);
    
    upper_slider.style.background = "url(" + imgNext + ")";
    upper_slider.style.backgroundSize = "cover";
    upper_slider.setAttribute('data-url', nextLink);

    // timer = setInterval(function () {KSTransitionTimer(imgNext)}, 100);
    KSTransitionTimer(imgNext);
} 

function KSSlideRight ( image, imgNext, nextLink) {
    
    codeAddress();
    upper_slider.innerHTML = "";
    upper_slider.style.width = "auto";
    upper_slider.style.height = "200px";

    var iDiv = document.createElement('div');
    iDiv.className = 'slideRight';
    iDiv.style.width = "auto";
    iDiv.style.height = "200px";
    upper_slider.appendChild(iDiv);

    var imagePart = document.createElement('img');
    imagePart.src = image;
    imagePart.width = "100px";
    imagePart.height = "100px";
    iDiv.appendChild(imagePart);

    upper_slider.style.background = "url(" + imgNext + ")";
    upper_slider.style.backgroundSize = "cover";
    upper_slider.setAttribute('data-url', nextLink);

    // timer = setInterval(function () {KSTransitionTimer(imgNext)}, 100);
    KSTransitionTimer(imgNext);
} 

window.onload = codeAddress();
