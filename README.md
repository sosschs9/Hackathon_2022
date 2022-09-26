# [2022 대구를 빛내는 해커톤] 달려라, 달구벌
### 자유세션 - 기존 저상버스 및 피크시간대 버스 이용 문제 해결

## 1.프로젝트 한 줄 설명
![image](https://user-images.githubusercontent.com/93771689/192135502-67eee04e-a4a5-4e02-8b2c-fd5b6ec443b6.png)
> 달려라, 달구벌 : 저스 좌석을 예약하고 기사님께 알려줘요!

직접 분석한 효율적인 노선 버스의 좌석을 편하게 예약하고, 타고자 하는 저상버스의 기사님께 예약 메세지를 보낼 수 있는 서비스입니다.

## 2. 주제
> 프로젝트 주제 : 버스 예약 시스템
기존 버스 시스템에서 혼잡시간대의 버스 만원 문제 및 저상버스의 저조한 탑승률 문제를 해결함으로써 대구 시민의 교통 편의성을 높이기 위한 서비스를 제안합니다.

## 3. 프로젝트 목적 및 배경
대한민국에서는 현재 구축되어있는 버스 노선에 따라 움직이는 버스를 버스정류장에서 타고 이동하는 일반적인 교통 시스템을 가지고 있습니다. 하지만 대도시에 속하는 대구광역시에는 지하철 호선도 타 대도시에 비해 적을 뿐더러, 기존의 대구 버스 시스템에서는 교통 약자를 위한 저상버스를 이용하기 어려운 환경이었습니다.  
저희 팀이 발견한 문제는 아래와 같습니다. 

#### 1st, 유동인구가 많은 버스 시간대에 버스를 이용하기 어려운 환경입니다.
대부분의 버스 시스템이 그러하듯, 많은 이들이 타는 노선에는 1시간에 5-6대의 버스가, 적은 이들이 타는 노선에는 1시간에 2-3대의 버스가 다니며, 배차 간격을 조절합니다. 하지만 어느 노선대이든, 오전 6-9시의 출근시간대, 저녁 5-8시의 퇴근시간대는 유동인구가 급증함으로써 원하는 버스를 타지 못하거나, 대부분은 좁은 버스에서 서서 긴 시간을 이동해야합니다. 

특히, 대구광역시의 경우에는 지하철이 3호선까지 밖에 없기 때문에 수도권이나 부산 등의 타 대도시에 비해 더욱 더 버스 유동인구가 많은 편입니다. 이로인해, 피크시간대 대부분의 사람들이 버스를 이용하지 못하는 불편함을 겪고 있는 상태입니다.

또한, 노선이 효율적이지 못해 적은 이들이 들리는 정류장을 자주 들려 길을 돌아가거나, 많은 이들이 내리지 않는 정류장인데 버스가 하나하나 멈춰서야 하여, 비효율적으로 길을 돌아가는 경우도 많습니다.

따라서, '달려라, 달구벌'에서는 기존 노선의 문제점을 해결한 새로운 노선을 제작하고, 이를 이용에 불편함을 겪었던 기존의 문제점을 해결한 버스의 좌석 예약 시스템을 새롭게 제공하고자 합니다.

#### 2nd, 교통 약자를 위한 저상버스 운영이 이용률이 저조하고 비효율적이라는 점입니다.
저상버스는 휠체어 등을 이용하는 교통약자들을 위해 버스의 높낮이가 조금 더 낮고 뒷문의 내리막 형태를 이용해 휠체어를 타서 이용할 수 있습니다. 하지만, 타지역 뿐 아니라 대구광역시에서는 저상버스의 이용률이 낮은 편입니다. 

교통 약자들이 이용하고 싶어도 버스 기사가 이를 보지 못하고 지나치는 경우가 많은 것 또한  그 이유 중 하나입니다. 이로 인해, 저상버스가 운행하는 시간대에 맞추어 버스정류장에 있더라도 이용하지 못하고 교통약자 콜택시를 이용하는 실정이 대부분입니다. 

따라서, '달려라, 달구벌' 에서는 저상버스를 이용하는 교통약자들의 불편함을 개선하여 타고싶은 버스를 예약하고 이를 버스기사에게 직접 예약 메세지를 보내 알릴 수 있는 효과적인 버스 시스템을 제공하고자 합니다.


## 4. 기능
> 전체 정류장 및 버스 조회
한 정류장을 입력하면 해당 정류장에 오는 버스의 번호와 그 정류장을 기준으로 도착까지 남은 시간을 알 수 있습니다. 

> 버스 좌석 예약 시스템
1. 원하는 버스의 번호를 입력하고 해당 노선을 확인합니다. 
2. 해당 노선에 포함된 정류장의 출발지와 도착지를 입력합니다.(정확한 버스 정류장 명을 기입해야 합니다.)
3. 원하는 좌석을 입력합니다.
4. 전체 선택 내역을 확인합니다.
5. 본인임을 알 수 있도록 id(이름)와 비밀번호를 입력합니다.
6. 최종적으로 예약합니다.

> 저상버스 예약 알림
1. 원하는 저상버스의 번호를 입력하고 해당 노선을 확인합니다.
2. 본인이 원하는 출발지와 도착지를 정합니다.
3. 전체 내역을 확인 후 '예약하기' 버튼을 누릅니다.
4. 기사님께 예약 메세지가 전송됩니다. (전송되었다는 팝업창이 뜹니다.)

> 추후 제작할 기능
- 선결제 시스템을 도입하기 위해 모바일 뱅킹 서비스를 추가할 예정입니다.


## 5. 활용방안과 기대효과
대구광역시라는 대도시에 맞지 않은 좁은 버스 시스템과 이용률이 저조할 수 밖에 없는 저상버스 시스템 문제를 해결할 수 있는 예약시스템을 통해 기존의 시민들의 불편함을 개선하고 삶의 질을 높이며, 장애인과 비장애인의 거리가 더 가까워질 수 있도록 사회를 변화시키고 싶습니다.

결과적으로 위에서 제시한 기능과 함께 아래와 같은 사회적 효과를 기대하고 있습니다. 
1. 좌석예약서비스의 기대효과는 다음과 같습니다.
- 만차로 인한 버스 확보 어려움 해결
- 출근 시간 단축
- 정류장에서 줄서기의 불편함 해결
- 승객 분산효과로 인한 입석률 감소
이렇듯, 기존의 문제점을 전반적으로 해결할 수 있어 이용자들의 삶의 질과 만족도가 상승될 것 입니다.
2. 저상버스 예약 알림 서비스의 기대효과는 다음과 같습니다.
- 장애인의 교통버스 이용률 증가 및 만족도 상승
- 저상버스 알림 서비스를 통한 장애인의 이동시간 단축
- 장애인의 버스 확보 어려움 해결
3. 전반적으로 이전보다 편리한 교통 시스템이 구축되면서, 대구 시민들이 이동 시간 및 삶의 만족도 향상에 큰 도움이 될것이라 예상됩니다.


## 6. 프로젝트에 활용된 기술
#### [기술 스택]
<디자인>
* figma *

<프론트>
* html, css, figma, ![API](https://github.com/ilhaera/Daegu-bus-API)

<서버>
* nodejs, flask, django, js, mongodb *

### 1. CI/CD
* 저희가 대구 버스에 관한 공공데이터를 분석하여 주요 장소를 지나가도록 새롭게 구축한 3개의 노선의 정류장과 고유 ID, 시간, 배차간격 등의 모든 데이터를 MongoDB에 넣어 저희만의 새로운 노선 데이터베이스를 구축합니다. 
* 비공식 API에서 불러온 저상버스와 일반 노선의 버스 정류장, 버스번호, ID, 배차간격 등의 시간 등 모든 정보를 호출합니다. 저희가 이용하는 호출한 데이터의 목록은 다음과 같습니다. 
(비공식 API 코드는 저희 팀이 원하는 모든 정보를 가져오지 못해 engine.js의 수정이 있었습니다.
- 버스 고유id => 버스 이름, 버스 노선, 버스 현재 위치, 차 번호(저상)
- 버스 이름 => 버스 이름, 버스 고유 id, 버스 방면
- 정류장 고유 id => 정류장 이름, 버스 방면, 버스 고유 id, 버스 방향, {차 번호(저상), 버스 현재 위치, 남은 정류장 개소, 남은 시간}
- 정류장 이름 => 정류장 이름, 정류장 고유 id
* flask 기반으로 해당 데이터베이스와 API, front의 template을 합쳐 모든 정보를 수신하고받아 연결시킵니다. 

- *Team: 밥친구들*
- *collaborator: 송혜경, 유지예, 제유나, 하재현*

### 2. 일반 버스의 예약 시스템 구축 - 데이터베이스
> 예약버스 운행 정보 저장 DB
> 예약 내역 DB
> 버스별 예약 현황 DB

### 3. 저상버스 및 일반 버스 노선 호출 - API 활용
대구버스 API - 비공식 REST API
> 개요 :  대구버스는 공개 API를 제공하지 않아 github의 비공식 API를 활용하게 되었습니다.
대구 버스정보서비스를 스크래핑, 파싱 후 json 형태로 반환하는 서비스를 활용하였고, 이를 파이썬으로 받아와 요청한 데이터를 웹페이지에 띄울 수 있도록 하였습니다. 
![달려라, 달구벌 API](https://github.com/sosschs9/Hackathon_2022/tree/jaehyeon/Daegu-bus-API)


## 7. 기타 설정
* requirements.txt(Hackathon_2022 / requirements.txt)
* nodejs
* flask

1. node(index.js) 실행 후 flask 실행
'''설치파일
pip install -r requirements 
'''

## 8. Contributor

### 팀명 : 밥친구들

### 디자인
| Name | Major |
|---|---|
| 유지예 | 컴퓨터학부 글로벌sw융합전공 |
[Figma](https://www.figma.com/file/UZALfz8tZvbNpgmQrcV8Xl/Untitled?node-id=0%3A1)


> ![image](https://user-images.githubusercontent.com/93771689/192135835-66000eed-aff9-42e3-8ae4-d9b8491174b1.png)


### 프론트
| Name | Major |
|---|---|
| 유지예 | 컴퓨터학부 글로벌sw융합전공 |
| 제유나 | 컴퓨터학부 글로벌sw융합전공 |
| 송혜경 | 컴퓨터학부 글로벌sw융합전공 |
| 하재현 | 컴퓨터학부 글로벌sw융합전공 |

### 백엔드
| Name | Major |
|---|---|
| 제유나 | 컴퓨터학부 글로벌sw융합전공 |
| 송혜경 | 컴퓨터학부 글로벌sw융합전공 |
| 하재현 | 컴퓨터학부 글로벌sw융합전공 |


### DB
| Name | Major |
|---|---|
| 제유나 | 컴퓨터학부 글로벌sw융합전공 |


## 9. 시연 영상
https://youtu.be/JtuXjqsvJPQ 전체 영상
https://youtu.be/fFwKoqUyHWw 예약 관련 화면 수정 후 영상

<타임 스탬프>
(mongoDB Atlas - 7번 참조)
1. nodejs 실행
2. flask 실행
> 예약버스 선택
1. 원하는 버스 번호 입력
2. 해당 버스의 노선 확인 후 방향 설정, 출발지, 도착지 입력
3. 본인의 선택 내역 확인
4. 본인의 이름 및 비밀번호 입력
5. 예약 완료
> 저상버스 선택
1. 원하는 버스 번호 입력
2. 해당 버스 노선 확인
3. 출발지, 도착지 입력
4. 전체 내역 확인
5. 확인 후 기사님께 전송하는 '예약하기' 버튼 누르기
6. 기사님께 전송 완료

(hyegoooong, jaehyeon, main(last commit) branch 봐주시면 되겠습니다.)
