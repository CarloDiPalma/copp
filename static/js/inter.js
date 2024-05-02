let d = document;


// const makeDark = [d.querySelector('.container'),d.querySelector('.header_below_wrapper'),d.querySelector('.header_wrapper')[0]]


const makeDark = {
    fullStory: d.querySelector('.fullStory'),
    cont: d.querySelector('.container'),
    headBelow: d.querySelector('.header_below_wrapper'),
    head: d.querySelector('.header_wrapper'),
    footer: d.querySelector('footer'),
    upWhite: d.querySelectorAll('.makeWhite'),
    prog_unit: d.querySelectorAll('.prog_unit_sh'),
    vacancy: d.querySelectorAll('.vacancy'),
    registration: d.querySelectorAll('.registration-detail'),
    login: d.querySelectorAll('.login-detail'),
    sign_up_button: d.querySelectorAll('.sign_up'),
    login_button: d.querySelectorAll('.login'),
    program_detail: d.querySelectorAll('.program_detail'),
    // fullStory: d.querySelector('.fullStory'),
    // fullStory_inner_text: d.querySelectorAll('.fullStory_inner_text'),
}

if(localStorage.getItem('isdark')){
    darkmode()
}



d.querySelector('#theme_mode').addEventListener('click',darkmode)

function darkmode(){
     
    if(makeDark.cont.classList.contains('darkmode')){
        d.querySelector('#change_theme').src = "/static_root/images/mode_night.svg";
        localStorage.removeItem('isdark')
    }

    else{
        d.querySelector('#change_theme').src = "/static_root/images/change_theme.svg";
        localStorage.setItem('isdark', true)
        
    }

    makeDark.footer.classList.toggle('border_top');
    makeDark.headBelow.classList.toggle('border_bottom');

    for(let i in makeDark){
        if(makeDark[i]==undefined) continue
        if(makeDark[i][0] == undefined){
            if(makeDark[i].length === 0){continue}
                 makeDark[i].classList.toggle('darkmode');
        }

        else if(makeDark[i][0] != undefined){
                for(let j =0; j<makeDark[i].length;j++){
                    if(makeDark[i] != makeDark.upWhite){
                        makeDark[i][j].classList.toggle('darkmode')
                        makeDark[i][j].classList.toggle('border')
                }
                
                else if(makeDark[i] == makeDark.upWhite){
                    makeDark[i][j].classList.toggle('white')
                }
            }
            
        }               
       
    }

}



