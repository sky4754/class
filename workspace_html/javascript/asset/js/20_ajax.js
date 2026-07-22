window.addEventListener('load', bind)

function bind(){

    const btn1 = document.querySelector('#btn1')
    btn1.addEventListener('click', function(){
        
        // 1. ajax 객체 생성
        const xhr = new XMLHttpRequest()

        // 2. 보낼 준비
        // 방식method, 주소
        xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

        // 3. 보내기
        xhr.send()

        xhr.onload = function(){
            console.log('다녀왔어')
            console.log( xhr.responseText )

            // 깜짝 퀴즈
            // 두 번째 사람의 이름을 출력
            //      Ervin Howell
            // 세 번째 사람의 lat를 출력
            //      -68.6102
            const member = JSON.parse(xhr.responseText)
            console.log(member[1])
            // console.log(member[1].name)
            console.log(member[1]['name'])
            console.log(member[2]['address']['geo']['lat'])
        }
    })
    const btn2 = document.querySelector('#btn2')
    btn2.addEventListener('click', function(){

        const xhr = new XMLHttpRequest()

        xhr.open('GET', '19_json.html')

        xhr.send()

        xhr.onload = function(){
            console.log('다녀왔어')
            console.log( xhr1.responseText )
        }
    })
    const btn3 = document.querySelector('#btn3')
    btn3.addEventListener('click', function(){
        
        const key = '54e5c68cdfdea1fdb8f272c58510cf5110a7e059836ac9fbb207e09cef28cdb4'
        let url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst'
        url += '?'
        url += 'serviceKey='+key
        url += '&numOfRows=1000'
        url += '&pageNo=1'
        url += '&dataType=JSON'
        url += '&base_date=20260722'
        url += '&base_time=1500'
        url += '&nx=63'
        url += '&ny=110'
        
        const xhr = new XMLHttpRequest()

        xhr.open('GET', url)

        xhr.send()

        xhr.onload = function(){
            // console.log('다녀왔어')
            console.log( xhr.responseText )
            const data = JSON.parse( xhr.responseText )
            console.log( data )

            console.log( data.response.body.items.item[0].category)
            console.log( data.response.body.items.item[0].fcastValue)
            console.log( data.response.body.items.item[0].fcstTime)

            // category가 T1H(기온), RN1(강수량), REH(습도)
            let item = data.response.body.items.item
            // for(let i=0; i<item.length; i++){
            //     if(item[i].category == 'T1H'){
            //         console.log(item[i])
            //     } else if(item[i].category == 'RN1'){
            //     console.log(item[i])
            //     } else if(item[i].category == 'REH'){
            //     console.log(item[i])
            //     }
            // }
            let filtered = item.filter(function(data){
                if(data.category == 'T1H'
                    || data.category == 'RN1'
                    || data.category == 'REH'){
                    return true
                }
            })
            console.log(filtered)

            // 문제1
            // 예측카테고리 | 예측시간 | 값
            const result1 = document.querySelector('#result1')

            filtered.forEach(function(we){
                const tr = document.createElement('tr');

                const categoryTd = document.createElement('td');
                const timeTd = document.createElement('td');
                const valueTd = document.createElement('td');

                categoryTd.innerText = we.category;
                timeTd.innerText = we.fcstTime;
                valueTd.innerText = we.fcstTime;

                tr.append(categoryTd);
                tr.append(timeTd);
                tr.append(valueTd);
 
                result1.append(tr)
            })
            
            
            // 문제2
            // 시간 | 온도(T1H) | 습도(REH) | 강수량(PTY)
            
        }
    })
}