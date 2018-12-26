import PySimpleGUIWx as sg

"""
    System Tray Icon
    Your very own peronsal status monitor in your system tray
    Super easy to use.
    1. Find an icon file or use this default
    2. Create your menu defintion
    3. Add if statements to take action based on your input

"""

logo = b'iVBORw0KGgoAAAANSUhEUgAAACEAAAAgCAMAAACrZuH4AAAABGdBTUEAALGPC/xhBQAAAwBQTFRFAAAAMGmYMGqZMWqaMmubMmycM22dNGuZNm2bNm6bNG2dN26cNG6dNG6eNW+fN3CfOHCeOXGfNXCgNnGhN3KiOHOjOXSjOHSkOnWmOnamOnanPHSiPXakPnalO3eoPnimO3ioPHioPHmpPHmqPXqqPnurPnusPnytP3yuQHimQnurQn2sQH2uQX6uQH6vR32qRn+sSXujSHynTH2mTn+nSX6pQH6wTIGsTYKuTYSvQoCxQoCyRIK0R4S1RYS2Roa4SIe4SIe6SIi7Soq7SYm8SYq8Sou+TY2/UYStUYWvVIWtUYeyVoewUIi0VIizUI6+Vo+8WImxXJG5YI2xZI+xZ5CzZJC0ZpG1b5a3apW4aZm/cZi4dJ2/eJ69fJ+9XZfEZZnCZJzHaZ/Jdp/AeKTI/tM8/9Q7/9Q8/9Q9/9Q+/tQ//9VA/9ZA/9ZB/9ZC/9dD/9ZE/tdJ/9dK/9hF/9hG/9hH/9hI/9hJ/9hK/9lL/9pK/9pL/thO/9pM/9pN/9tO/9tP/9xP/tpR/9xQ/9xR/9xS/9xT/91U/91V/t1W/95W/95X/95Y/95Z/99a/99b/txf/txh/txk/t5l/t1q/t5v/+Bb/+Bc/+Bd/+Be/+Bf/+Bg/+Fh/+Fi/+Jh/+Ji/uJk/uJl/+Jm/+Rm/uJo/+Ro/+Rr/+Zr/+Vs/+Vu/+Zs/+Zu/uF0/uVw/+dw/+dz/+d2/uB5/uB6/uJ9/uR7/uR+/uV//+hx/+hy/+h0/+h2/+l4/+l7/+h8gKXDg6vLgazOhKzMiqrEj6/KhK/Qka/Hk7HJlLHJlLPMmLTLmbbOkLXSmLvXn77XoLrPpr/Tn8DaocLdpcHYrcjdssfZus/g/uOC/uOH/uaB/uWE/uaF/uWK/+qA/uqH/uqI/uuN/uyM/ueS/ueW/ueY/umQ/uqQ/uuS/uuW/uyU/uyX/uqa/uue/uye/uyf/u6f/uyq/u+r/u+t/vCm/vCp/vCu/vCy/vC2/vK2/vO8/vO/wtTjwtXlzdrl/vTA/vPQAAAAiNpY5gAAAQB0Uk5T////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AFP3ByUAAAAJcEhZcwAAFw8AABcPASe7rwsAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuMWMqnEsAAAKUSURBVDhPhdB3WE1xHMdxt5JV0dANoUiyd8kqkey996xclUuTlEKidO3qVnTbhIyMW/bee5NskjJLmR/f3++cK/94vP76Ps/n/Zx7z6mE/6koJowcK154vvHOL/GsKCZXkUgkWlf4vWGWq5tsDz+JWIzSokAiqXGe7nWu3HxhEYof7fhOqp1GtptQuMruVhQdxZ05U5G47tYUHbQ4oah6Fg9Z4ubm7i57JhQjdHS0RSzUPoG17u6zZTKZh8c8XlytqW9YWUOH1LqFOZ6enl5ec+XybFb0rweM1tPTM6yuq6vLs0lYJJfLvb19fHwDWGF0jh5lYNAe4/QFemOwxtfXz8/fPyBgwVMqzAcCF4ybAZ2MRCexJGBhYGBQUHDw4u1UHDG1G2ZqB/Q1MTHmzAE+kpCwL1RghlTaBt/6SaXS2kx9YH1IaOjSZST8vfA9JtoDnSngGgL7wkg4WVkofA9mcF1Sx8zMzBK4v3wFiYiMVLxlEy9u21syFhYNmgN7IyJXEYViNZvEYoCVVWOmUVvgQVSUQqGIjolRFvOAFd8HWVs34VoA+6OjY2JjY5Vxm4BC1UuhGG5jY9OUaQXci1MqlfHx8YmqjyhOViW9ZsUN29akJRmPFwkJCZsTSXIpilJffXiTzorLXYgtcxRJKpUqKTklJQ0oSt9FP/EonxVdNY4jla1kK4q2ZB6mIr+AipvduzFUzMSOtLT09IyMzMxtJKug/F0u/6dTexAWDcXXLGEjapKjfsILOLKEuYiSnTQeYCt3UHhbwEHjGMrETfBJU5zq5dSTcXC8hLJccSWP2cgLXHPu7cQNAcpyxF1dyjehAKb0cSYUAOXCUw6V8OFPgevTXFymC+fPPLU677Nw/1X8A/AbfAKGulaqFlIAAAAASUVORK5CYII='

menu_def = ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']]

tray = sg.SystemTray(menu=menu_def, data_base64=logo)

tray.ShowMessage('Starting', 'Now Starting the application')

while True:
    event = tray.Read()
    if event == 'Exit':
        break
    elif event == 'Menu':       # add your checks here
        pass
    tray.ShowMessage('Event', '{}'.format(event))