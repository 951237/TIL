# TIL - 자바스크립트 200515
### innerHtml : 내부 html 코드를 javascript 코드에서 변경할 수 있음.

```
<script type = "text/javascript">
    function innerHtmlTest() {
        var randValNode = document.getElementById("rand_val");
        randValNode.innerHtml = "<b><font color = 'red'>" + Math.Random() + "</font></b>"
    }
<script>
```