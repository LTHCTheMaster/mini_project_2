let open_py = document.getElementById("open_py");
let go_end = document.getElementById("go_end");

function sys_over () {
    open_py.onclick = function () {
        open("files/crypto.py");
    }
    go_end.onclick = function () {
        window.scrollBy(0, 100000);
    }
}

sys_over();
