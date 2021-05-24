const getRandomHexaColor = () => {
    const hexa = '0123456789abcdef';
    var color = '#';
    for (i=0; i < 6; i++) {
        color += hexa[Math.floor(Math.random() * 16)];
    }
    return color;
};



setInterval(() => { 
    document.querySelector('body').style.backgroundColor = 
    getRandomHexaColor();
}, 100);






const clockContent = document.querySelector('.now');
        const getCurrentTime = () => {
                        const date = new Date();
            console.log(date);
            
            const year = date.getFullYear();

            const month = date.getMonth();

            const clockDate = date.getDate();

            const day = date.getDay();
                                 
            const hours = date.getHours();

            const minutes = date.getMinutes();

            const seconds = date.getSeconds();

            clockContent.innerText = `${year}년 ${month+1}월 ${clockDate}일` +

            ` ${hours < 10 ? `0${hours}` : hours}시 ${minutes < 10 ? `0${minutes }`  : minutes }분 ${seconds < 10 ? `0${seconds }`  : seconds }초`;

        };
        
        const initClock = () => {
            getCurrentTime();
            setInterval(getCurrentTime, 1000);
        };

        initClock();