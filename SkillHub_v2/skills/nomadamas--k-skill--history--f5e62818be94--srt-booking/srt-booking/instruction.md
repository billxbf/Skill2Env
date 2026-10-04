# SRT Live Timetable Lookup

## What this skill does

`SRTrain`의 시간표 검색 경로를 이용해 현재 SRT 운행 후보와 일반실·특실 예약 가능 여부를 조회한다.

이 스킬은 회원 로그인 불필요한 **라이브 조회 전용**이다.

- `auto_login=False` 익명 client를 사용한다.
- NetFunnel 대기열과 시간표 검색 요청만 실행한다.
- 예약, 예약대기, 좌석 선점, 결제, 취소, 자동 재조회는 실행하지 않는다.
- 정확한 호차·좌석번호를 조회하지 않는다.
- 구매는 공식 SRT 페이지에서 사용자가 직접 진행한다.

실행 환경에는 Python 3.11 이상과 `uv`가 필요하다. `uv`가 없으면 공식 설치 문서를 안내하고 조회를 실행하지 않는다.

## Commands

```bash
npx -y @nomadamas/k-skill@0 exec srt-booking scripts/srt_booking.py -- \
  search \
  --dep 수서 \
  --arr 부산 \
  --date 20260819 \
  --time 0600 \
  --time-limit 1200 \
  --limit 5
```

현재 라이브 조회 endpoint와 안전 경계:

```bash
npx -y @nomadamas/k-skill@0 exec srt-booking scripts/srt_booking.py -- source
```

출력:

- 열차번호·열차종류
- 출발역·도착역
- 현재 출발·도착 시각
- 일반실·특실 예약 가능 여부
- 사용한 라이브 search endpoint
- 공식 SRT 페이지

## Workflow

1. 출발역, 도착역, 날짜, 시간대를 확인한다.
2. `search`를 한 번 실행한다. `수서역`처럼 `역`이 붙은 입력은 helper가 표준 역명으로 정규화한다.
3. 현재 운행 후보를 제시한다.
4. 좌석 구매가 필요하면 `booking_url`을 제공하고 종료한다.
5. 사용자가 다시 요청하지 않는 한 polling·매진 감시를 시작하지 않는다.

## Hard boundaries

- `KSKILL_SRT_ID`, `KSKILL_SRT_PASSWORD` 또는 회원 로그인을 요구하지 않는다.
- helper에 `reserve`, `reservations`, `cancel`, `payment`, waiting-list 명령을 추가하지 않는다.
- 예약 endpoint, 결제 endpoint 또는 계정 endpoint를 호출하지 않는다.
- NetFunnel key를 예약·선점 자동화에 사용하지 않는다.
- CAPTCHA·접근 거부·계정 제한이 발생하면 즉시 중단한다.
- 사용자 요청 한 번을 반복 수집이나 장기 실행으로 확장하지 않는다.

## Failure modes

- NetFunnel 대기 또는 SRT 접근 제한
- `SRTrain` 설치·호환성 문제
- 날짜·시간 또는 역명 오류
- 조건에 맞는 열차 없음

이 경우 차단을 우회하지 않고 [SRT 공식 조회 페이지](https://etk.srail.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000)를 안내한다.

## Legal notice

```bash
npx -y @nomadamas/k-skill@0 read srt-booking references/AUTOMATION-LEGAL-STATEMENT.md
```
