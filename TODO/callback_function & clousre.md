# 콜백 함수
- 자바스크립트에서는 함수도 하나의 자료형이므로 매개변수로 전달할 수 있다.
- 이렇게 매개변수로 전달하는 함수를 콜백 함수라고 합니다.

# 클로저
- 함수를 리턴하는 함수를 이용한다.
- 지역 변수는 함수가 실행될 때 생성되고 함수가 종료될 때 사라진다라는 규칙을 위반할 수 있다.

```
<script type="text/javascript">
	function test(name){
		var output = 'Hello ' + name + ' .. !';
		
		return function(){
			alert(output);
		};
	}
	test('abc')();
</script>
```
