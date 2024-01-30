def on_status_reached_comparison_lt_type_percentage(status):
    mySprite2.set_scale(1.5, ScaleAnchor.MIDDLE)
    mySprite3.scale = 1.3
statusbars.on_status_reached(StatusBarKind.health,
    statusbars.StatusComparison.LT,
    statusbars.ComparisonType.PERCENTAGE,
    50,
    on_status_reached_comparison_lt_type_percentage)

def on_a_pressed():
    animation.run_image_animation(mySprite,
        [img("""
                ........................
                        ....ffffff..............
                        ..ffeeeef2f.............
                        .ffeeeef222f............
                        .feeeffeeeef...cc.......
                        .ffffee2222ef.cdc.......
                        .fe222ffffe2fcddc.......
                        fffffffeeeffcddc........
                        ffe44ebf44ecddc.........
                        fee4d41fddecdc..........
                        .feee4dddedccc..........
                        ..ffee44e4dde...........
                        ...f222244ee............
                        ...f2222e2f.............
                        ...f444455f.............
                        ....ffffff..............
                        .....fff................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ........................
                        .......fff..............
                        ....fffff2f.............
                        ..ffeeeee22ff...........
                        .ffeeeeee222ff..........
                        .feeeefffeeeef..........
                        .fffffeee2222ef.........
                        fffe222fffffe2f.........
                        fffffffffeeefff.....cc..
                        fefe44ebbf44eef...ccdc..
                        .fee4d4bbfddef..ccddcc..
                        ..feee4dddddfeecdddc....
                        ...f2222222eeddcdcc.....
                        ...f444445e44ddccc......
                        ...ffffffffeeee.........
                        ...fff...ff.............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                .......ff...............
                        ....ffff2ff.............
                        ..ffeeeef2ff............
                        .ffeeeeef22ff...........
                        .feeeeffeeeef...........
                        .fffffee2222ef..........
                        fffe222ffffe2f..........
                        ffffffffeeefff..........
                        fefe44ebf44eef..........
                        .fee4d4bfddef...........
                        ..feee4dddee.c..........
                        ...f2222eeddeccccccc....
                        ...f444e44ddecddddd.....
                        ...fffffeeee.ccccc......
                        ..ffffffff...c..........
                        ..fff..ff...............
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """),
            img("""
                ....ffffff..............
                        ..ffeeeef2f.............
                        .ffeeeef222f............
                        .feeeffeeeef............
                        .ffffee2222ef...........
                        .fe222ffffe2f...........
                        fffffffeeefff...........
                        ffe44ebf44eef...........
                        fee4d41fddef............
                        .feee4ddddf.............
                        ..fdde444ef.............
                        ..fdde22ccc.............
                        ...eef22cdc.............
                        ...f4444cddc............
                        ....fffffcddc...........
                        .....fff..cddc..........
                        ...........cdc..........
                        ............cc..........
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
                        ........................
            """)],
        100,
        False)
    if mySprite.overlaps_with(mySprite2):
        statusbar.value += -5
        mySprite.x += -100
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

mySprite3: Sprite = None
statusbar: StatusBarSprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999111199999999999999999999999999999999999999999999999999999999999999999999999999999911119999999999999999999999999999999999999999999999999999
        9999999999999999999991111119999999999999999999999999999999999999999999999999999999999999999999999999999111111999999999999999999999999999999999999999999999999999
        9999999999999999999991111119911999999999999999999999999999999999999999999999999999999999999999999999999111111991199999999999999999999999999999999999999999999999
        9999999999999999991111111119111119999999999999999999999999999999999999999999999999999999999999999999111111111911111999999999999999999999999999999999999999999999
        9999999999999999911111111111111119999999999999999999999999999999999999999999999999999999999999999991111111111111111999999999999999999999999999999999999999999999
        9999999999999999111111111111111111199999999999999999999999999999999999999999999999999999999999999911111111111111111119999999999999999999999999999999999999999999
        9999999999999999111111111111111111119999999999999999999999999999999999999999999999999999999999999911111111111111111111999999999999999999999999999999999999999999
        9999999999999999911111111111111111119991199999999999999999999999999999999999999999999999999999999991111111111111111111999119999999999999999999999999999999999999
        9999999999999111191111111111111111119911111999999999999999999999999999999999999999999999999999911119111111111111111111991111199999999999999999999999999999999999
        9999999999991111119111111111111111199911111999999999999999999999999999999999999999999999999999111111911111111111111119991111199999999999999999999999999999999999
        9999999999991111111111111111111111911111111199999999999999999999999999999999999999999999999999111111111111111111111191111111119999999999999999999999999999999999
        9999999999991111111111111111111111111111111199999999999999999999999999999999999999999999999999111111111111111111111111111111119999999999999999999999999999999999
        9999999999999111111111111111111111111111111199999999999999999999999999999999999999999999999999911111111111111111111111111111119999999999999999999999999999999999
        9911199991111911111111111111111111111111111991199999999999991111999999999999999999991119999111191111111111111111111111111111199119999999999999111199999999999999
        9111119911111111111111111111111111111111111911119999999999911111199999999999999999911111991111111111111111111111111111111111191111999999999991111119999999999999
        9111119111111111111111111111111111111111111911119999999999911111191119999999999999911111911111111111111111111111111111111111191111999999999991111119111999999999
        9911111111111111111111111111111111111111111111119999999999999111111111999999999999991111111111111111111111111111111111111111111111999999999999911111111199999999
        9111111111111111111111111111111111111111111111199999999911119111111111999999999999911111111111111111111111111111111111111111111119999999991111911111111199999999
        1111111111111111111111111111111111111111111111119999999111111111111119999999999199111111111dd1111111111111111111111111111111111111999999911111111111111999999999
        1111111111111111111111111111111111111111111111111911199111111111111111111999999ddd111111111ddd111111111111111111111111111111111111191119911111111111111111199999
        1111111111111111111111111111111111111111111111111111111111111111111111111199991ddd111111111ddd111111111111111111111111111111111111111111111111111111111111119999
        11111111111111111111111111111111111111111111111111111111111111111111111111999ddddddd111111ddddd11111111111111111111111111111111111111111111111111111111111119999
        11111111111111111111111111111111111111111ddddddddd111111111111111111111111111ddddddd111111ddddd111111111111111111111111111111111111111111dddddddddd1111111111111
        11111111111111111111111111111111111111111ddddddddd111111111111111111111111111ddddddd111111ddddd111111111111111111111111111111111111111111dddddddddd1111111111111
        1111111111111111111ddd1111111111111111111d11dddddd111111111111111111111111111d11dddd11111ddddddd11111111111111111111dd1111111111111111111dd1d1ddddd1111111111111
        111111111111111111ddddd111111111111111111ddddddd1d111111111111111111111111111ddddddd11111ddddddd1111111111111111111dddd111111111111111111dddddd11dd1111111111111
        11111111111111111dddddd111111111111111111ddddddddd1111111111d11111111ddddd111d1ddddd11111ddddddd11111111111111111dddddd111111111111111111dddddddddd1111111111111
        11111111111111111ddd1d111111d111111111111ddddddddd111111111dd11111111ddddd111ddddddd11111ddddddd11111111111111111ddd1d111111dd11111111111dddd1ddddd11111111dd111
        11111111111111111dddddd11111d111111111111ddddddd1d111111111dd11111111ddddd111ddddddd11111ddddddd11111111111111111dddddd11111dd11111111111ddddddd1dd11111111dd111
        11111111ddd111111dd11d11111ddd11111111111ddddddddd11dddddd1dd11111111ddddd111ddddddd11111ddddddd111111111dd111111ddd1d11111ddd11111111111dddddddddd1ddddddddd111
        d1dd1111ddddddddddd1ddd111ddddd1111111111ddddddd1d11d11ddd1dd111111111dd1dd11ddddddd111dddddddddd1dd1111ddddddddddddd1d1111dddd1111111111dddddd11dd1d11dddddd111
        dddd11111d1dd1ddddddddd111ddddd1111111111ddddddddd11dddd1d1dd11111111dddddd11dd1dddd111ddddddddddddd1111dd1ddd1dddddddd1111dddd1111111111dddddddddd1dddd1dddd111
        dd1d11111ddd1111ddddddd111ddddd1111111111ddddddddd11dddd1dddd11111111dddddd11ddddddd111ddddddddddd1d1111dddd1d11ddddddd1111dddd1111111111dddddddddd1dddd1dddd111
        dddd1111dddddddddddddddd11dddddd11dd1dd1ddddddddddd1d11dddddd11111111dddddd11ddddddd111ddddddddddddd1111dddddddddddddddd11dddddd111d11ddddddddddddd1d11dddddd111
        dd1d1111dddddddddddddddd11dddddd11ddddddddddddddddd1ddddddddd11d11d11dddddd11ddddddd111ddddddddddd1d1111dddddddddddddddd11dddddd111dddddddddddddddd1ddddddddd111
        ddddd1dd1d1ddddddddddddd11ddddddd1dddd11ddddddddddddd11bbddddddd1ddd11dd1dd11ddddddd111ddddddddddddddd1ddd1ddddddddddddd11ddddddd111d11ddddddbddddddd11bbbddd1dd
        ddddd1dddddddddddddddddddd1dddddd1dddddddddbbbdddddddddbbbdddddd1ddd1dddddd11ddddddd111ddddddddddddddd1dddddddddddddddddddddddddd1ddddddddddbbdddddddddbbbddd1dd
        ddddd1ddddddddddddddddddddddddddd1dddddddddbbbdddddddddbbbdddddddddddddddddddddddddd111ddddddddddddddd1dddddddddddddddddddddddddd1ddddddddddbbdddddddddbbbdddddd
        ddddd1ddddddddddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddd1dddddddddddddddddddddddddd1d1ddddddbbbbbbbdddddbbbbbddddd
        dddddbbbbbbbbbddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddd1ddddddddbbbbbbbdddddbbbbbddddd
        dddddbbbbbbbbbddddddddddddddddddd1dddddddbbbbbbbddddddbbbbbddddddddddddddddddddddddddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddd1ddddddddbbbbbbbdddddbbbbbddddd
        dddddbddbbbbbbddddddddddddddddddd1dddddddbddbbbbdddddbbbbbbbdd111dddddddddddddddbbdddd1ddddddddddddddbbdbdbbbbbdddddddddddddddddd1ddddddddbbbbbbbddddbbbbbbbb11d
        dddddbbbbbbbdbddddddddddddddddddd1dddddddbbbbbbbdddddbbbbbbbddd11ddddddddddddddbbbbddd1ddddddddddddddbbbbbbddbbdddddddddddddddddd1ddddddddbbbbbbbddddbbbbbbbbddd
        dddddbbbbbbbbbddddddddddbddddddddbbbbbdddbdbbbbbdddddbbbbbbbddddddddddd1dddddbbbbbbddd1ddddddddddddddbbbbbbbbbbdddddddddddddddddddbbbbddddbbbdbbbddddbbbbbbbbddd
        dddddbbbbbbbbbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd1ddddddddddddddbbbdbddddddbbdddddddddddbbbbdbbbbbddddddddbbdddddddddbbbbddddbbbdbbbddddbbbbbbbbd1d
        dddddbbbbbbbdbdddddddddbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdd111ddddddddddddbbbbbbdddddbbdddddddddddbbbbbbbdbbddddddddbbddddddddbbbbbbdddbbbbbbbddddbbbbbbbb11d
        dddddbbbbbbbbbddbbbbbbdbbddddddddbbbbbdddbbbbbbbdddddbbbbbbbdddddddddbb1dddddbbbdbdddddbbbdddddddddddbbbbbbbbbbdbbbbbbbbbddddddddbbbbbbdddbbbdbbbddddbbbbbbbbddd
        dddddbbbbbbbdbddbddbbbdbbdddddddddbbdbbddbbbbbbbdddbbbbbbbbbbdbbddddbbbbbbbbbbbbbdbddddbbbbddddddddddbbbbbbddbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        dddddbbbbbbbbbddbbbbdbdbbddddddddbbbbbbddbbdbbbbdddbbbbbbbbbbbbbddddbbdbbbdbbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
        dddddbbbbbbbbbddbbbbdbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbdbddbbbbbbbddddbbbbddddddddddbbbbbbbbbbdbbbbdbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        dbbdbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbddbbbbbbbdddbbbbbbbbbbbbbddddbbbbbbbbbbbbbbbbddbbbbbbdddbddbbbbbbbbbbbbbdbddbbbbbbddddddddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbdbbbbbbbbbddbddbddbbbbbbddbbbbbbbdddbbbbbbbbbbbdbddddbbbbbbbbbbbbbbbbddbbbbbbdddbbbbbbbbbbbbbbbbdbbbbbbbbbdddddbddbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbddbbbbbbbbbbbbbddddbbbbbbbdbbbddbbdbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbdbbbbbbbbbbbbbddbbbbbbbdddbddbbbbbbbbbbbbbbddbdbbbbdbbdbbbdbbbbbbbddbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbdbbbbbbddbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbdbbbbbbbbbbbddbbbbdbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbddbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbdddbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbddbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbbbbbbbb7bbbbbbbbbbbbbbbb7bbbbb
        bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7bbbbbb7bbb77bbbbb77bbbb7bbb7bbbb7b77bbb7
        bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77bb7bbb77b77bb7bbb77bbb77bbb77bbb7bb77b77
        bb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777bbb77bb77b77bb77bbb77b77bbbb77b7b77b7777b
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
"""))
mySprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.change_scale(0.5, ScaleAnchor.MIDDLE)
mySprite2 = sprites.create(assets.image("""
    myImage0
"""), SpriteKind.enemy)
mySprite2.set_scale(1, ScaleAnchor.MIDDLE)
mySprite.y = 100
mySprite2.x = 150
mySprite2.y = 100
statusbar = statusbars.create(50, 4, StatusBarKind.health)
statusbar.position_direction(CollisionDirection.RIGHT)
statusbar2 = statusbars.create(20, 4, StatusBarKind.health)
statusbar2.position_direction(CollisionDirection.LEFT)
mySprite3 = sprites.create(img("""
        . . f f f . . . . . . . . f f f 
            . f f c c . . . . . . f c b b c 
            f f c c . . . . . . f c b b c . 
            f c f c . . . . . . f b c c c . 
            f f f c c . c c . f c b b c c . 
            f f c 3 c c 3 c c f b c b b c . 
            f f b 3 b c 3 b c f b c c b c . 
            . c b b b b b b c b b c c c . . 
            . c 1 b b b 1 b b c c c c . . . 
            c b b b b b b b b b c c . . . . 
            c b c b b b c b b b b f . . . . 
            f b 1 f f f 1 b b b b f c . . . 
            f b b b b b b b b b b f c c . . 
            . f b b b b b b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . .
    """),
    SpriteKind.projectile)
mySprite3.scale = 0.5

def on_forever():
    pause(1000)
    if statusbar2.value < 1:
        animation.run_image_animation(mySprite,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 3 1 3 . . . . . . 
                                . . . . . . 2 3 1 3 2 . . . . . 
                                . . . . . . 2 1 1 1 2 . . . . . 
                                . . . . . . 2 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 2 3 1 3 2 . . . . . 
                                . . . . . . . 2 2 2 . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 2 3 3 3 3 3 2 . . . . 
                                . . . . 3 1 1 1 1 1 1 1 3 . . . 
                                . . . . 1 1 1 1 1 1 1 1 1 . . . 
                                . . . 2 1 1 1 1 1 1 1 1 1 2 . . 
                                . . . 2 3 1 1 1 1 1 1 3 3 2 . . 
                                . . . . . . 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 4 4 4 4 4 . . . . . . 
                                . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                                . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                                . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                                . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                                . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                                . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                                . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                                . . . 2 2 4 d 5 5 d d 4 4 . . . 
                                . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                                . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                                . . . . . 2 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                                . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                                . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                                . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                                . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                                2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                                2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                                4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                                . . b b b b 2 4 4 2 b b b b . . 
                                . b d d d d 2 4 4 2 d d d d b . 
                                b d d b b b 2 4 4 2 b b b d d b 
                                b d d b b b b b b b b b b d d b 
                                b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                                . . b b d d 1 1 3 d d 1 b b . . 
                                . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                                . . . 2 2 4 4 4 4 4 2 2 2 . . .
                """),
                img("""
                    . . . . . . . . b b . . . . . . 
                                . . . . . . . . b b . . . . . . 
                                . . . b b b . . . . . . . . . . 
                                . . b d d b . . . . . . . b b . 
                                . b d d d b . . . . . . b d d b 
                                . b d d b . . . . b b . b d d b 
                                . b b b . . . . . b b . . b b . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . b b b d d d d d d b b b . . 
                                . b d c c c b b b b c c d d b . 
                                b d d c b . . . . . b c c d d b 
                                c d d b b . . . . . . b c d d c 
                                c b d d d b b . . . . b d d c c 
                                . c c b d d d d b . c c c c c c 
                                . . . c c c c c c . . . . . . .
                """)],
            200,
            False)
        pause(700)
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
        sprites.destroy_all_sprites_of_kind(SpriteKind.status_bar)
        game.splash("You lose")
forever(on_forever)

def on_forever2():
    if mySprite.x < 0:
        mySprite.x = 0
forever(on_forever2)

def on_forever3():
    if True:
        pass
forever(on_forever3)

def on_forever4():
    pause(1000)
    if statusbar.value < 1:
        animation.run_image_animation(mySprite2,
            [img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 2 1 2 . . . . . . 
                                . . . . . . . 3 1 3 . . . . . . 
                                . . . . . . 2 3 1 3 2 . . . . . 
                                . . . . . . 2 1 1 1 2 . . . . . 
                                . . . . . . 2 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 3 1 1 1 3 . . . . . 
                                . . . . . . 2 3 1 3 2 . . . . . 
                                . . . . . . . 2 2 2 . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 2 3 3 3 3 3 2 . . . . 
                                . . . . 3 1 1 1 1 1 1 1 3 . . . 
                                . . . . 1 1 1 1 1 1 1 1 1 . . . 
                                . . . 2 1 1 1 1 1 1 1 1 1 2 . . 
                                . . . 2 3 1 1 1 1 1 1 3 3 2 . . 
                                . . . . . . 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . 4 4 4 4 4 . . . . . . 
                                . . . 4 4 4 5 5 5 d 4 4 4 4 . . 
                                . . 4 d 5 d 5 5 5 d d d 4 4 . . 
                                . . 4 5 5 1 1 1 d d 5 5 5 4 . . 
                                . 4 5 5 5 1 1 1 5 1 1 5 5 4 4 . 
                                . 4 d d 1 1 5 5 5 1 1 5 5 d 4 . 
                                . 4 5 5 1 1 5 1 1 5 5 d d d 4 . 
                                . 2 5 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . 2 d 5 5 d 1 1 1 5 1 1 5 5 2 . 
                                . . 2 4 d d 5 5 5 5 d d 5 4 . . 
                                . . . 2 2 4 d 5 5 d d 4 4 . . . 
                                . . 2 2 2 2 2 4 4 4 2 2 2 . . . 
                                . . . 2 2 4 4 4 4 4 4 2 2 . . . 
                                . . . . . 2 2 2 2 2 2 . . . . .
                """),
                img("""
                    . . . . 2 2 2 2 2 2 2 2 . . . . 
                                . . . 2 4 4 4 5 5 4 4 4 2 2 2 . 
                                . 2 2 5 5 d 4 5 5 5 4 4 4 4 2 . 
                                . 2 4 5 5 5 5 d 5 5 5 4 5 4 2 2 
                                . 2 4 d d 5 5 5 5 5 5 d 4 4 4 2 
                                2 4 5 5 d 5 5 5 d d d 5 5 5 4 4 
                                2 4 5 5 4 4 4 d 5 5 d 5 5 5 4 4 
                                4 4 4 4 . . 2 4 5 5 . . 4 4 4 4 
                                . . b b b b 2 4 4 2 b b b b . . 
                                . b d d d d 2 4 4 2 d d d d b . 
                                b d d b b b 2 4 4 2 b b b d d b 
                                b d d b b b b b b b b b b d d b 
                                b b d 1 1 3 1 1 d 1 d 1 1 d b b 
                                . . b b d d 1 1 3 d d 1 b b . . 
                                . . 2 2 4 4 4 4 4 4 4 4 2 2 . . 
                                . . . 2 2 4 4 4 4 4 2 2 2 . . .
                """),
                img("""
                    . . . . . . . . b b . . . . . . 
                                . . . . . . . . b b . . . . . . 
                                . . . b b b . . . . . . . . . . 
                                . . b d d b . . . . . . . b b . 
                                . b d d d b . . . . . . b d d b 
                                . b d d b . . . . b b . b d d b 
                                . b b b . . . . . b b . . b b . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . b b b d d d d d d b b b . . 
                                . b d c c c b b b b c c d d b . 
                                b d d c b . . . . . b c c d d b 
                                c d d b b . . . . . . b c d d c 
                                c b d d d b b . . . . b d d c c 
                                . c c b d d d d b . c c c c c c 
                                . . . c c c c c c . . . . . . .
                """)],
            200,
            False)
        pause(700)
        sprites.destroy_all_sprites_of_kind(SpriteKind.player)
        sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
        sprites.destroy_all_sprites_of_kind(SpriteKind.projectile)
        sprites.destroy_all_sprites_of_kind(SpriteKind.status_bar)
        game.splash("You win")
forever(on_forever4)

def on_forever5():
    if mySprite.overlaps_with(mySprite3):
        statusbar2.value += -2
forever(on_forever5)

def on_forever6():
    if mySprite.y < 74:
        mySprite.y = 72
forever(on_forever6)

def on_forever7():
    for index in range(5):
        mySprite2.y += 5
        pause(100)
    for index2 in range(5):
        mySprite2.y += -5
        pause(100)
    for index3 in range(4):
        mySprite2.y += -5
        pause(100)
    for index4 in range(4):
        mySprite2.y += 5
        pause(100)
forever(on_forever7)

def on_forever8():
    animation.run_image_animation(mySprite3,
        [img("""
                . . f f f . . . . . . . . f f f 
                        . f f c c . . . . . . f c b b c 
                        f f c c . . . . . . f c b b c . 
                        f c f c . . . . . . f b c c c . 
                        f f f c c . c c . f c b b c c . 
                        f f c 3 c c 3 c c f b c b b c . 
                        f f b 3 b c 3 b c f b c c b c . 
                        . c b b b b b b c b b c c c . . 
                        . c 1 b b b 1 b b c c c c . . . 
                        c b b b b b b b b b c c . . . . 
                        c b c b b b c b b b b f . . . . 
                        f b 1 f f f 1 b b b b f c . . . 
                        f b b b b b b b b b b f c c . . 
                        . f b b b b b b b b c f . . . . 
                        . . f b b b b b b c f . . . . . 
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . f f f . . . . . . . . . . . 
                        f f f c c . . . . . . . . f f f 
                        f f c c . . c c . . . f c b b c 
                        f f c 3 c c 3 c c f f b b b c . 
                        f f b 3 b c 3 b c f b b c c c . 
                        . c b b b b b b c f b c b c c . 
                        . c b b b b b b c b b c b b c . 
                        c b 1 b b b 1 b b b c c c b c . 
                        c b b b b b b b b c c c c c . . 
                        f b c b b b c b b b b f c . . . 
                        f b 1 f f f 1 b b b b f c c . . 
                        . f b b b b b b b b c f . . . . 
                        . . f b b b b b b c f . . . . . 
                        . . . f f f f f f f . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . c c . . c c . . . . . . . . 
                        . . c 3 c c 3 c c c . . . . . . 
                        . c b 3 b c 3 b c c c . . . . . 
                        . c b b b b b b b b f f . . . . 
                        c c b b b b b b b b f f . . . . 
                        c b 1 b b b 1 b b c f f f . . . 
                        c b b b b b b b b f f f f . . . 
                        f b c b b b c b c c b b b . . . 
                        f b 1 f f f 1 b f c c c c . . . 
                        . f b b b b b b f b b c c . . . 
                        c c f b b b b b c c b b c . . . 
                        c c c f f f f f f c c b b c . . 
                        . c c c . . . . . . c c c c c . 
                        . . c c c . . . . . . . c c c c 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . f f f . . . . . . . . f f f . 
                        f f c . . . . . . . f c b b c . 
                        f c c . . . . . . f c b b c . . 
                        c f . . . . . . . f b c c c . . 
                        c f f . . . . . f f b b c c . . 
                        f f f c c . c c f b c b b c . . 
                        f f f c c c c c f b c c b c . . 
                        . f c 3 c c 3 b c b c c c . . . 
                        . c b 3 b c 3 b b c c c c . . . 
                        c c b b b b b b b b c c . . . . 
                        c b 1 b b b 1 b b b b f c . . . 
                        f b b b b b b b b b b f c c . . 
                        f b c b b b c b b b b f . . . . 
                        . f 1 f f f 1 b b b c f . . . . 
                        . . f b b b b b b c f . . . . . 
                        . . . f f f f f f f . . . . . .
            """)],
        700,
        True)
forever(on_forever8)

def on_forever9():
    pause(1000)
    mySprite3.x = mySprite2.x
    mySprite3.y = mySprite2.y
    for index5 in range(9):
        mySprite3.x += -20
        pause(100)
forever(on_forever9)

def on_forever10():
    if mySprite.y > 125:
        mySprite.y = 124
forever(on_forever10)
