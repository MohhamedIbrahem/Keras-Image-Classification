const imageInput = document.getElementById("imageInput");

const previewImage = document.getElementById("previewImage");

const uploadContent = document.getElementById("uploadContent");

const loading = document.getElementById("loading");

const result = document.getElementById("result");


imageInput.addEventListener("change", function(){

    const file = this.files[0];

    if(file){

        previewImage.src = URL.createObjectURL(file);

        previewImage.style.display = "block";
        
        if (uploadContent) {
            uploadContent.style.display = "none";
        }
    }
});


async function predictImage(){

    const file = imageInput.files[0];

    if(!file){

        alert("Please upload image first");

        return;
    }

    loading.style.display = "flex";

    result.style.display = "none";

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch("/predict",{

        method:"POST",

        body:formData
    });

    const data = await response.json();

    loading.style.display = "none";

    result.style.display = "block";

    document.getElementById("predictionText").innerHTML =

        `${data.prediction}`;

    document.getElementById("confidenceText").innerHTML =

        `Confidence Score: ${data.confidence}%`;
}