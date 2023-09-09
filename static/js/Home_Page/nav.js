const media = () => {
    let q = matchMedia("(max-width:900px)");
    const sdnav = document.getElementById('sidenav');
    if (q.matches) {
        document.querySelector('sidenav')
        
        const toggleButton = document.getElementById('menu');
        
        sdnav.style.display = 'none';
        
        toggleButton.addEventListener('click', () => {
            if (sdnav.style.display === 'none') {
                sdnav.style.display = 'block';
                sdnav.style.position = 'fixed';
                sdnav.style.width = '30vh';
            }
            else {
                sdnav.style.display = 'none';
            }
        });
    }
    else {
        sdnav.style.display = "block";
        sdnav.style.position = 'sticky';
        sdnav.style.width = '120vh';
    }
}
onload = media;
onresize = media;