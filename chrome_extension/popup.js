function injectTheScript() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        // query the active tab, which will be only one tab
        //and inject the script in it
        chrome.tabs.executeScript(tabs[0].id, {file: "content_script.js"});
    });
}
document.getElementById('clickactivity').addEventListener('click', injectTheScript);




// function waitLoad(callback) {
//     chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
//         let timer = setInterval(() => {
//             chrome.tabs.executeScript(tabs[0].id, {
//                 file: "content_script.js"
//             }, (data) => {
//                 console.log('Calling at ' + new Date().toLocaleString().replace(',',''));
//                 callback()
//                 clearInterval(timer)
//             })
//         }, 5000)
//     })
// }
// document.getElementById('clickactivity').addEventListener('click', waitLoad);

