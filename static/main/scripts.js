//Запрос к хероку



let isMenuShow;
isMenuShow  = true;


let slider_img_width_landing = 354;
let position_slider_landing = 0;

let  slider_img_width_photoshop = 354;
let position_slider_photoshop = 0;

let slider_img_width_illustrator = 354;
let position_slider_illustrator = 0;

let  slider_img_width_ui = 354;
let position_slider_ui = 0;

let  slider_img_width_photo = 354;
let position_slider_photo = 0;

let  slider_img_width_pd = 354;
let position_slider_pd = 0;


window.addEventListener('scroll', function(){
    if(window.pageYOffset != '0'){
        document.getElementById('5').style.boxShadow = ('0 0 10px black');
        document.getElementById('5').style.transition = ('0.2s');
    }
    else{
        document.getElementById('5').style.boxShadow = ('none');
        document.getElementById('5').style.transition = ('0');
        
    }
});

function LoginButt(){
    document.location.href = "/registration/login";
}


function MainButt(){
    document.location.href = "registration/login";
}

function TestAuto(){
    document.location.href = "registration/login";
}

window.onload = function Onload_Profile(){
    document.getElementById('55').style.opacity = ('1');
}

function CreteProject(){
    document.location.href = "/addwork/addwork/";   
}

function All_work_profile(){
    
    document.getElementById('list_common').style.display=('block');
    document.getElementById('list_like').style.display=('none');
    document.getElementById('All_work_profile').style.background=('#c70202');
    document.getElementById('Like_work_profile').style.background=('white');
    document.getElementById('Like_work_profile').style.color=('#c70202');
    document.getElementById('All_work_profile').style.color=('white');
    

}

function Like_work_profile(){
    document.getElementById('list_common').style.display=('none');
    document.getElementById('list_like').style.display=('block');
    document.getElementById('All_work_profile').style.background=('white');
    document.getElementById('Like_work_profile').style.background=('#c70202');
    document.getElementById('Like_work_profile').style.color=('white');
    document.getElementById('All_work_profile').style.color=('#c70202');
}



//МиниГалерея кнопки вправо и влево




function right_button_landing(){
    position_slider_landing-=slider_img_width_landing;
    if(position_slider_landing==-1040){
        document.getElementById('right_button_label').style.display = ('none');
    }
    document.getElementById('sliders_cont_landing').style.marginLeft = (position_slider_landing + 'px');
    document.getElementById('sliders_cont_landing').style.transition = ('0.4s');
    document.getElementById('left_button_label').style.display = ('block');
    document.getElementById('right_button_label').style.position = ('absolute');

}

function left_button_landing(){
    position_slider_landing+=slider_img_width_landing;
    document.getElementById('sliders_cont_landing').style.marginLeft = (position_slider_landing + 'px');
    document.getElementById('sliders_cont_landing').style.transition = ('0.4s'); 
    if(position_slider_landing==0){
        document.getElementById('left_button_label').style.display = ('none');
        document.getElementById('right_button_label').style.position = ('relative');

    }
        document.getElementById('right_button_label').style.display = ('block');
        
}




function right_button_photoshop(){
    position_slider_photoshop-=slider_img_width_photoshop;
    if(position_slider_photoshop==-1040){
        document.getElementById('right_button_label_photoshop').style.display = ('none');
    }
    document.getElementById('sliders_cont_photoshop').style.marginLeft = (position_slider_photoshop + 'px');
    document.getElementById('sliders_cont_photoshop').style.transition = ('0.4s');
    document.getElementById('left_button_label_photoshop').style.display = ('block');
    document.getElementById('right_button_label_photoshop').style.position = ('absolute');

}

function left_button_photoshop(){
    position_slider_photoshop+=slider_img_width_photoshop;
    document.getElementById('sliders_cont_photoshop').style.marginLeft = (position_slider_photoshop + 'px');
    document.getElementById('sliders_cont_photoshop').style.transition = ('0.4s'); 
    if(position_slider_photoshop==0){
        document.getElementById('left_button_label_photoshop').style.display = ('none');
        document.getElementById('right_button_label_photoshop').style.position = ('relative');

    }
        document.getElementById('right_button_label_photoshop').style.display = ('block');
        
}


function right_button_illustrator(){
    position_slider_illustrator-=slider_img_width_illustrator;
    if(position_slider_illustrator==-1040){
        document.getElementById('right_button_label_illustrator').style.display = ('none');
    }
    document.getElementById('sliders_cont_illustrator').style.marginLeft = (position_slider_illustrator + 'px');
    document.getElementById('sliders_cont_illustrator').style.transition = ('0.4s');
    document.getElementById('left_button_label_illustrator').style.display = ('block');
    document.getElementById('right_button_label_illustrator').style.position = ('absolute');

}

function left_button_illustrator(){
    position_slider_illustrator+=slider_img_width_illustrator;
    document.getElementById('sliders_cont_illustrator').style.marginLeft = (position_slider_illustrator + 'px');
    document.getElementById('sliders_cont_illustrator').style.transition = ('0.4s'); 
    if(position_slider_illustrator==0){
        document.getElementById('left_button_label_illustrator').style.display = ('none');
        document.getElementById('right_button_label_illustrator').style.position = ('relative');

    }
        document.getElementById('right_button_label_illustrator').style.display = ('block');
        
}



function right_button_ui(){
    position_slider_ui-=slider_img_width_ui;
    if(position_slider_ui==-1040){
        document.getElementById('right_button_label_ui').style.display = ('none');
    }
    document.getElementById('sliders_cont_ui').style.marginLeft = (position_slider_ui + 'px');
    document.getElementById('sliders_cont_ui').style.transition = ('0.4s');
    document.getElementById('left_button_label_ui').style.display = ('block');
    document.getElementById('right_button_label_ui').style.position = ('absolute');

}

function left_button_ui(){
    position_slider_ui+=slider_img_width_ui;
    document.getElementById('sliders_cont_ui').style.marginLeft = (position_slider_ui + 'px');
    document.getElementById('sliders_cont_ui').style.transition = ('0.4s'); 
    if(position_slider_ui==0){
        document.getElementById('left_button_label_ui').style.display = ('none');
        document.getElementById('right_button_label_ui').style.position = ('relative');

    }
        document.getElementById('right_button_label_ui').style.display = ('block');
        
}




function right_button_photo(){
    position_slider_photo-=slider_img_width_photo;
    if(position_slider_photo==-1040){
        document.getElementById('right_button_label_photo').style.display = ('none');
    }
    document.getElementById('sliders_cont_photo').style.marginLeft = (position_slider_photo + 'px');
    document.getElementById('sliders_cont_photo').style.transition = ('0.4s');
    document.getElementById('left_button_label_photo').style.display = ('block');
    document.getElementById('right_button_label_photo').style.position = ('absolute');

}

function left_button_photo(){
    position_slider_photo+=slider_img_width_photo;
    document.getElementById('sliders_cont_photo').style.marginLeft = (position_slider_photo + 'px');
    document.getElementById('sliders_cont_photo').style.transition = ('0.4s'); 
    if(position_slider_photo==0){
        document.getElementById('left_button_label_photo').style.display = ('none');
        document.getElementById('right_button_label_photo').style.position = ('relative');

    }
        document.getElementById('right_button_label_photo').style.display = ('block');
        
}




function right_button_pd(){
    position_slider_pd-=slider_img_width_pd;
    if(position_slider_pd==-1040){
        document.getElementById('right_button_label_pd').style.display = ('none');
    }
    document.getElementById('sliders_cont_pd').style.marginLeft = (position_slider_pd + 'px');
    document.getElementById('sliders_cont_pd').style.transition = ('0.4s');
    document.getElementById('left_button_label_pd').style.display = ('block');
    document.getElementById('right_button_label_pd').style.position = ('absolute');

}

function left_button_pd(){
    position_slider_pd+=slider_img_width_pd;
    document.getElementById('sliders_cont_pd').style.marginLeft = (position_slider_pd + 'px');
    document.getElementById('sliders_cont_pd').style.transition = ('0.4s'); 
    if(position_slider_pd==0){
        document.getElementById('left_button_label_pd').style.display = ('none');
        document.getElementById('right_button_label_pd').style.position = ('relative');

    }
        document.getElementById('right_button_label_pd').style.display = ('block');
        
}




//Аватарка

const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const imageForm = document.getElementById('image-form')
const confirmBtn = document.getElementById('confirm-btn')
const input = document.getElementById('id_file')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
var video_el = document.getElementById('upload_img');

video_el.addEventListener('change', ()=>{
    alertBox.innerHTML = ""
    confirmBtn.classList.remove('not-visible')
    const img_data = video_el.files[0]
    const url = URL.createObjectURL(img_data)

    imageBox.innerHTML = `<img src="${url}" id="image" width="700px" class="imagebbg">`
    var $image = $('#image')
    console.log($image)
    

    $image.cropper({
    aspectRatio: 9 / 9,
    crop: function(event) {
        console.log(event.detail.x);
        console.log(event.detail.y);
        console.log(event.detail.width);
        console.log(event.detail.height);
        console.log(event.detail.rotate);
        console.log(event.detail.scaleX);
        console.log(event.detail.scaleY);
    }
})


var cropper = $image.data('cropper');
    confirmBtn.addEventListener('click', ()=>{
        cropper.getCroppedCanvas().toBlob((blob) => {
            console.log('confirmed')
            const fd = new FormData();
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            fd.append('image', blob, 'my-image.png');

            $.ajax({
                type:'POST',
                url: imageForm.action,
                enctype: 'multipart/form-data',
                data: fd,
                success: function(){
                    console.log('збс')
                },
                error: function(error){
                    console.log('error', error)
                },
                complete:function(){
                    window.location.reload();
                },
                cache: false,
                contentType: false,
                processData: false,
                
            })
        })
        
    })

document.getElementById('jojo').style.display = ('block')
document.getElementById('jojo').style.pointerEvents = ('auto')
})


function closeModalWin(){
     document.getElementById('jojo').style.display = ('none')
}





function adaptiveFunction() {
    if (isMenuShow )
{
    document.getElementById('jet').style.display = ('flex')
    isMenuShow  = false;
}
else
{
    document.getElementById('jet').style.display = ('none')
    
isMenuShow  = true;
}
};

