// let observer = new MutationObserver(mutations => {
//     console.log("mutations count: " + mutations.length);

//     // for(let mutation of mutations) {
//     //      for(let addedNode of mutation.addedNodes) {
//     //          console.log(addedNode);
             
//     //       }
//     //  }
//  });
// observer.observe(document, { childList: true, subtree: true });

var slots_found = false;

function click18_button(){
    var buttons18 = document.getElementsByClassName("form-check-label");
    buttons18[0].click();
    console.log("18+ button clicked at " + new Date().toLocaleString().replace(',',''));
}

function getRowCount(){
    var uls = document.getElementsByClassName("slot-available-wrap");
    var available = document.querySelectorAll('.slots-box:not(.no-seat):not(.no-available)')
    console.log("UL count: " + uls.length + " , available = " + available.length + " at " + new Date().toLocaleString().replace(',',''));
    if(available.length > 1){
        slots_found = true;
        playSound();
        // alert('Found available slot!!');
    }

    // // var buttons18 = document.getElementsByClassName("form-check-label");
    //     // for (var j = 0; j < buttons18.length; j++) {
    //     //     first_button18 = buttons18[j];
    //     //     first_button18.click();
    //     //     console.log(j + ' : 18+ Clicked at ' + new Date().toLocaleString().replace(',',''));
    //     //     sleep(500);

    //         var els = document.querySelectorAll(".slots-box:not(.no-seat)");
    //         var withSeats = document.querySelectorAll(".slots-box");
    //         var byClassName = document.getElementsByClassName("slots-box");

    //         console.log("withSeats : " + withSeats.length + " . Without seats = " + els.length + " . byClassName seats = " + byClassName.length);
    //         // for (var k = 0; k < els.length; k++) {
    //         //     var el = els[k];
    //         //     alert('Found available slot!!')
    //         //     break;
    //         // }
    //     //     break;
    //     // }
}

function findSlotAvailableButtonRecursive() {
    var max = 1;
    while(max < 5){
        max = max + 1;

        var buttons = document.getElementsByClassName("pin-search-btn");
        buttons[0].click();
        console.log(max + ' : Search button clicked at ' + new Date().toLocaleString().replace(',',''));   
        setTimeout(function(){ click18_button(); }, 3000);

        setTimeout(function(){ getRowCount(); }, 500);
        if(slots_found === true){
            break;
        }
           
    }    
}

function playSound(){
    var myAudio = new Audio(chrome.runtime.getURL("beep.mp3"));
    myAudio.play();
}

function selectStateAndDistrict(){
    

    //switch to 'search by district'
    console.log("switch to search by district");
    document.getElementsByClassName("status-switch")[0].click();

    //Selet state drop-down
    console.log("select state drop-down");
    document.querySelectorAll('.mat-select')[0].click();

    // Selct Maharashtra     mat-option-21
    console.log("select Maharashtra");
    var options = document.querySelectorAll('.mat-option');
    for(var i = 0; i < options.length; i++){
        // console.log(options[i].id);
        if(options[i].id == "mat-option-21"){
            options[i].click();
            break;
        }
    }
    // document.querySelectorAll('.mat-option')[0].click();
    // document.getElementsByClassName("mat-option-text")[20].click();

    //Selet district drop-down   
    
    document.querySelectorAll('.mat-select')[1].focus();

    var ev = document.createEvent('KeyboardEvent');
    // Send key '13' (= enter)
    ev.initKeyboardEvent(
        'keypress', true, true, window, false, false, false, false, 80, 0);
    document.body.dispatchEvent(ev);

    // document.querySelectorAll('.mat-select')[1].click();
    // var dropdowns = document.querySelectorAll('.mat-select');
    // for(var i = 0; i < dropdowns.length; i++){
    //     console.log(dropdowns[i].id);
    //     // if(i = 1){
    //     //     var xPathRes = document.evaluate ('//*[@id="mat-option-63"]/span', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
    //     //     xPathRes.singleNodeValue.click();
    //     // }
        
    //     if(dropdowns[i].id == "mat-select-2"){
    //         console.log(dropdowns[i].id);
    //         dropdowns[i].click();

    //         // var xPathRes = document.evaluate ('//*[@id="mat-option-63"]/span', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
    //         // xPathRes.singleNodeValue.click();

    //         // var options = dropdowns[i].querySelectorAll('.mat-option');
    //         // console.log(options.length);
    //         // for(var i = 0; i < options.length; i++){
    //         //     console.log(options[i].id);
    //         //     if(options[i].id == "mat-option-63"){
    //         //         options[i].click();
    //         //         break;
    //         //     }
    //         // }
    //         break;
    //     }
    //     break;
    // }

    // Selct Maharashtra
    // document.getElementsByClassName("mat-option-text")[1].click();
}

function findSlotAvailableButton() {
    var buttons = document.getElementsByClassName("pin-search-btn");
    for (var i = 0; i < buttons.length; i++) {
        first_button = buttons[i];
        //alert('clicking first_button')
        first_button.click();
        console.log(i + ' : Search button clicked at ' + new Date().toLocaleString().replace(',',''));
        setTimeout(function(){ getRowCount(); }, 2000);

        sleep(2000);

        break;
    }
}

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

// selectStateAndDistrict();

// for (var j = 0; j < 3; j++) {
//     console.log(j + ' : Trying at ' + new Date().toLocaleString().replace(',',''));
//     findSlotAvailableButton();
//     sleep(7000);
// }

// findSlotAvailableButton();

findSlotAvailableButtonRecursive();

// playSound();