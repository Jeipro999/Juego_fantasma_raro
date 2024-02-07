namespace SpriteKind {
    export const ProyectilFase2 = SpriteKind.create()
}
statusbars.onStatusReached(StatusBarKind.Health, statusbars.StatusComparison.LT, statusbars.ComparisonType.Percentage, 50, function (status) {
    mySprite2.setScale(1.5, ScaleAnchor.Middle)
    mySprite3.scale = 1.3
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    [],
    100,
    false
    )
    mySprite.startEffect(effects.fire, 1000)
    if (mySprite.overlapsWith(mySprite2)) {
        statusbar.value += -80
        if (Fases == 0) {
            mySprite.x += -100
        }
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Fases == 1) {
        animation.runImageAnimation(
        mySprite,
        [],
        300,
        false
        )
        pause(900)
        animation.runImageAnimation(
        mySprite,
        [],
        100,
        false
        )
        pause(500)
        animation.runImageAnimation(
        mySprite,
        [],
        1,
        false
        )
        pause(600)
    }
})
let mySprite5: Sprite = null
let Disparo_2 = 0
let mySprite4: Sprite = null
let mySprite3: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
let Fases = 0
let Win = 0
scene.setBackgroundImage()
Fases = 0
mySprite = sprites.create(assets.image`myImage`, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.changeScale(0.5, ScaleAnchor.Middle)
mySprite2 = sprites.create(assets.image`myImage0`, SpriteKind.Enemy)
for (let index = 0; index < 15; index++) {
    mySprite2.startEffect(effects.halo)
}
mySprite2.setScale(1, ScaleAnchor.Middle)
mySprite.y = 100
mySprite2.x = 150
mySprite2.y = 100
statusbar = statusbars.create(50, 4, StatusBarKind.Health)
statusbar.positionDirection(CollisionDirection.Right)
let statusbar2 = statusbars.create(20, 4, StatusBarKind.Health)
statusbar2.positionDirection(CollisionDirection.Left)
mySprite3 = sprites.create(, SpriteKind.Projectile)
mySprite3.scale = 0.5
forever(function () {
    if (Fases == 3) {
        mySprite2.y = randint(76, 120)
        mySprite2.x = randint(0, 160)
        pauseUntil(() => (8 as any) == (0 as any))
    } else {
    	
    }
})
forever(function () {
    if (Fases == 66) {
        mySprite.setPosition(85, 42)
    }
})
forever(function () {
    if (Fases == 3) {
        if (statusbar.value < 1) {
            Fases = 66
            sprites.destroy(statusbar)
            sprites.destroy(statusbar2)
            mySprite.setPosition(53, 68)
            mySprite2.setPosition(68, 42)
            mySprite2.sayText("Oye")
            pause(1300)
            mySprite.sayText("Si?")
            pause(1300)
            mySprite2.sayText("¿Por qué me matas?")
            pause(1300)
            mySprite.sayText("Es culpa del guión del videojuego")
            pause(1300)
            mySprite2.sayText("¿Y tu quieres matarme?")
            pause(1300)
            mySprite.sayText("No")
            pause(1300)
            mySprite2.sayText("¿Entonces?")
            pause(1300)
            mySprite.sayText("Tienes razon")
            pause(1300)
            mySprite.setScale(3, ScaleAnchor.Middle)
            animation.runImageAnimation(
            mySprite,
            [],
            200,
            false
            )
            pause(800)
            game.gameOver(false)
        }
    }
})
forever(function () {
    if (Fases == 1) {
        mySprite4 = sprites.create(, SpriteKind.ProyectilFase2)
        Disparo_2 = 1
        pauseUntil(() => Fases == -2131)
    }
})
forever(function () {
    pause(100)
    if (Fases == 3) {
        mySprite2.y = randint(76, 120)
        mySprite2.x = randint(0, 160)
        for (let index = 0; index < 4; index++) {
            mySprite2.startEffect(effects.halo)
        }
        pause(1800)
        animation.runImageAnimation(
        mySprite2,
        [],
        300,
        false
        )
        if (mySprite.overlapsWith(mySprite2)) {
            statusbar2.value += -5
        }
        pause(800)
        animation.runImageAnimation(
        mySprite2,
        [],
        0,
        false
        )
    }
})
forever(function () {
    if (Fases == 1) {
        if (statusbar.value < 1) {
            for (let index = 0; index < 10; index++) {
                statusbar.value += 10
                pause(100)
            }
            Fases = 3
            Disparo_2 = 5
            sprites.destroy(mySprite4)
        } else {
        	
        }
    }
})
forever(function () {
    pause(1000)
    if (statusbar2.value < 1) {
        mySprite.startEffect(effects.disintegrate)
        pause(500)
        sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
        sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
        sprites.destroyAllSpritesOfKind(SpriteKind.StatusBar)
        game.gameOver(false)
    }
})
forever(function () {
    if (mySprite.x < 0) {
        mySprite.x = 0
    }
})
forever(function () {
    if (Fases == 1) {
        if (mySprite.overlapsWith(mySprite4)) {
            if (controller.B.isPressed()) {
                mySprite5 = sprites.create(, SpriteKind.Projectile)
                mySprite5.setPosition(mySprite.x, mySprite.y)
                for (let index = 0; index < 7; index++) {
                    mySprite5.y += -18
                    pause(100)
                    if (mySprite2.overlapsWith(mySprite5)) {
                        statusbar.value += -100
                        sprites.destroy(mySprite5)
                    }
                }
                sprites.destroy(mySprite5)
            } else {
                if (mySprite.overlapsWith(mySprite4)) {
                    statusbar2.value += -40
                }
            }
        }
    }
})
forever(function () {
    if (mySprite.overlapsWith(mySprite3)) {
        statusbar2.value += -5
    }
})
forever(function () {
    pause(1000)
    if (statusbar.value < 1) {
        animation.runImageAnimation(
        mySprite2,
        [],
        200,
        false
        )
        animation.runImageAnimation(
        mySprite2,
        [],
        200,
        false
        )
        sprites.destroyAllSpritesOfKind(SpriteKind.Projectile)
        for (let index = 0; index < 10; index++) {
            statusbar.value += 10
            pause(100)
        }
        animation.runMovementAnimation(
        mySprite2,
        animation.animationPresets(animation.flyToCenter),
        400,
        false
        )
        animation.runImageAnimation(
        mySprite2,
        [],
        100,
        false
        )
        for (let index = 0; index < 4; index++) {
            mySprite2.y += -20
            pause(200)
        }
        pause(1500)
        Fases = 1
    }
})
forever(function () {
    if (mySprite.y < 74) {
        mySprite.y = 72
    }
})
forever(function () {
    if (Disparo_2 == 1) {
        animation.runImageAnimation(
        mySprite2,
        [],
        500,
        false
        )
        mySprite4.setPosition(mySprite2.x, mySprite2.y)
        pause(300)
        mySprite4.setPosition(mySprite.x, mySprite2.y)
        pause(300)
        for (let index = 0; index < 14; index++) {
            mySprite4.y += 10
            pause(100)
            mySprite4.startEffect(effects.fire)
            mySprite4.startEffect(effects.fire)
        }
        pause(1000)
    }
})
forever(function () {
    animation.runImageAnimation(
    mySprite3,
    [],
    700,
    true
    )
})
forever(function () {
    if (mySprite.y > 125) {
        mySprite.y = 124
    }
})
forever(function () {
    pause(randint(800, 1200))
    mySprite3.x = mySprite2.x
    mySprite3.y = mySprite2.y
    for (let index = 0; index < 9; index++) {
        mySprite3.x += -20
        pause(100)
    }
})
forever(function () {
    if (Fases == 0) {
        for (let index = 0; index < 5; index++) {
            mySprite2.y += 5
            pause(100)
        }
        for (let index = 0; index < 5; index++) {
            mySprite2.y += -5
            pause(100)
        }
        for (let index = 0; index < 4; index++) {
            mySprite2.y += -5
            pause(100)
        }
        for (let index = 0; index < 4; index++) {
            mySprite2.y += 5
            pause(100)
        }
    } else {
    	
    }
})
