from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
#list1-20

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                choices=PRODUCT_QUANTITY_CHOICES,
                coerce=int)
    update = forms.BooleanField(required=False,
                initial=False,
                widget=forms.HiddenInput)
#quantity：让用户可以在 1~20 之间选择产品的数量。
#我们使用了带有 coerce=int 的 TypeChoiceField 字段来把输入转换为整数
#update：让你展示数量是否要被加进已当前的产品数量上（False），
# 否则如果当前数量必须被用给定的数量给更新（True）。
# 我们为这个字段使用了HiddenInput 控件，因为我们不想把它展示给用户。