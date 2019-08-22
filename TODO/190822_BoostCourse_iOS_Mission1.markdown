* Mission1에서 헤맸던 점
- imageView에서 tapGesture를 달아줬는데, 아무리 해도 인식이 되지 않았다.
imageView.isUserInteactionEnable = true 로 함으로써 해결할 수 있었음.
- DateFormatter에서 "MMM dd, yyyy"로 dateFormat을 해줘야 함을 몰라서, 구글링을 통해 해결
MMM을 하게되면 Aug,March, April 이런식으로 표현이 가능하다
- Optional에 대한 이해가 부족하고, if let, guard에 대한 코드 연습이 부족함을 느꼈다.
즉, Optional에서 값을 어떻게 빼서 쓰고, nil인 경우에는 어떻게 처리해주어야 하는지 연습이 필요하다.
- 버튼을 어떻게 비활성화 처리해줘야 할지에 대해서도 헤맸다. 문서를 보는 법이 연습이 안돼 구글링을 해서 해결했다.
```
//버튼 비활성화
okButton.isUserInteractionEnabled = false
okButton.setTitleColor(UIColor.gray, for: .normal)
 okButton.setTitleColor(UIColor.gray, for: .disabled)
 ```
 위의 방식으로 처리하였다. 아직도 잘 이해는 안되지만, 이런식으로 disabled하고, 버튼 색을 바꾸는 식으로 클릭 처리를 막았다.

* Mission1 프로젝트에서 못한 내용
- 오토레이아웃 방법을 몰라서 시도도 하지 못함
- 뷰 컨트롤러 간 전환에 대해 확실히 이해 못해서, 비효율적으로 하고 있음.
- 뷰 컨트롤러 간 화면 전환에서 데이터를 끌고 다니는 법이 완벽하지 못함.

* 연습해야 하는 것
- 애플 문서 보는 법 연습
- 오토레이아웃 학습
- 뷰 컨트롤러 간 전환 방법 학습 (데이터 끌고 다니면서 전환하는 법, 화면 되돌리는 법)
- Optional 연습. if-let 구문 실습, guard 구문 실습.
