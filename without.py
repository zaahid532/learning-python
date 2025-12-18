import modules as ms
ms.greeting('zaahid')
msg = 'a module author is '+ms.author
print(msg)
from modules import greeting, author
greeting('zaahid')
msg = 'a module author is '+author
print(msg)