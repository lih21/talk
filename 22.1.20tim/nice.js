const nav = document.getElementsByClassName('nav')[0]
let lis = document.getElementsByClassName('lis')
console.log(lis);

window.onscroll = () => {
    let t = document.documentElement.scrollTop || document.body.scrollTop;
    if (t > 0) {
        nav.style.background = "#f5f5f5"
        for (i of lis) {
            i.style.color = "#247cff"
        }
    } else {
        nav.style.background = "none"
        for (i of lis) {
            i.style.color = "white"
        }
    }
}
window.onresize = () => {
    let bwidth = document.body.clientWidth;
    if (bwidth <= 1206) {
        nav.style.width = "1300px"
        document.getElementsByClassName("box")[0].style.width = "1300px"
    } else {
        nav.style.width = "100%"
        document.getElementsByClassName("box")[0].style.width = "100%"
    }
}