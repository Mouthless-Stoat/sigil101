# Chapter 3.1: The first of many

## Introduction

In this sub chapter we will be making a simple customs sigil that is basically a `Rabbit Hole` clone but they spawn ant instead. From this custom sigil we'll with customize it to be more complex.

This section Chapter 3.1 however will only touch one how to get your sigil loaded and have a test card ready, in the next section Chapter 3.2 is where we will make our sigil code and learn how to share our sigil as well.

> [!NOTE]
> "Game directory" and "Game File" mean the same thing they are whatever folder appear when you press the `Open Game Directory` on the main screen.
> "Game Code" refer to the actual game code that you open using the Godot Engine.

## Ceremony

> [!NOTE]
> Ceremony mean code that you always must write before implementing anything or your solution to a problem.

Let make an empty sigil file to start coding our sigil in. First go to your `File System` find the `scripts` folder open it then open the `classes` folder and lastly open the `sigils` folder. Now right click on the `sigils` folder and choose new script. Now name the file `Custom` and click create.

> [!NOTE]
> If you are using the alternate method of making sigils make a new file in your `scripts` in the game directory name `Custom` (the ending `.gd` is important)

After creating the file find the file in your `File System` double click to open it, now you should be in the script tab with the script open in front of you. You can delete everything in the file and type the following:

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	pass
```

Let break down what this code is doing the first line `extends SigilEffect` this will tell Godot that this is a sigil effect file. Next, if you remember from Chapter 1 we are defining a new function name `handle_event` with 2 parameters `event` and `params`.

`String` and `Array` are what we call type declaration, this tell Godot that `event` is supposed to be a type `String` and `params` is of type `Array`. This is unimportant for now but it help to make our code more clear about what variable supposed to be what.

```gdscript
func handle_event(event: String, params: Array):
```

Next in the body of the function we have `pass`, `pass` is basically a empty body but `gdscript` doesn't like an empty function we put in `pass` as a placeholder for now.

When a sigil activates the game call our `handle_event` function with the event name and some other parameter that we may want. `event` will be the event name that the sigil activate for and `params` will be the extra parameter. First we need check if our sigil activate because the card was summoned, put this as your function body:

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned":
		pass
```

This will see if our `event` is `card_summoned` which get call when a card get summoned. We once again use `pass` because we have not decide what we want to do yet. Let put a print statement in our body so we know that the sigil activated.

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned":
		print("Custom Activated")
```

Now let test the sigil, first we need to add a new card to test our sigil, to do this we should create a new ruleset to contain our test card.

## Testing sigil

> [!NOTE]
> If you are using the alternate method of making sigils skip this section

This is not mean to be a comprehensive guide to making ruleset so we will only make a simple ruleset to test our sigil. To make a custom ruleset navigate to your `rulesets` folder in the game directory. In this folder create a new file call `test.json` and in the file it with the following information:

```json
{
    "ruleset": "TEST",
    "hammers_per_turn": 1,
    "ant_limit": 100,
    "deck_size_min": 1,
    "max_commons_main": 4,
    "max_commons_side": 10,
    "num_candles": 3,
    "variable_attack_nerf": false,
    "allow_snuffing_candles": true,
    "opt_actives": false,
    "enable_backrow": false,
    "starting_bones": 100000,
    "stating_energy_max": 100000,
    "portrait": "portraits/Stoat",
    "description": "TEST TIME",
    "cards": [
        {
            "name": "Thick",
            "attack": 0,
            "health": 2,
            "sigils": ["Custom"]
        },
        {
            "name": "Squirrel",
            "attack": 0,
            "health": 1
        }
    ],
    "side_decks": {
        "10 Squirrels": {
            "type": "single",
            "card": "Squirrel",
            "count": 10
        }
    }
}
```

We use `Thick` as the card name here so we don't have to make the art for the card and just reuse the `Thick` card art you can use any other name that you like.We would also need art for the sigil you can make your own or use [this](https://raw.githubusercontent.com/Mouthless-Stoat/sigil101/main/3-rabbit/Ant%20Hill.png), after getting your art you can import it into the game. To import your sigil art into the game go to your `FileSystem` and open up the folder `gfx` then `sigils` and drag our file into this folder. Now we can load this ruleset in the game like how you would load any other ruleset but there is a couple other things we need to do so the game can load our sigil.

First go back to Godot and find the file `CardInfo.gd` and in there go to line `231`, you should see something like this:

```gdscript
...
	"Warded": "A card bearing this sigil takes only 1 damage from attacks and card effects.",
	"Waterborne": "A card bearing this sigil submerges itself during its opponent's turn. while submerged, opposing creatures attack its owner directly.",
	"Worthy Sacrifice": "A card bearing this sigil is counted as 3 blood rather than 1 blood when sacrificed."
}
...
```

Insert a new line after line `231` and add something like this.

> [!NOTE]
> The comma at the end of line `231` is important

```gdscript
...
	"Warded": "A card bearing this sigil takes only 1 damage from attacks and card effects.",
	"Waterborne": "A card bearing this sigil submerges itself during its opponent's turn. while submerged, opposing creatures attack its owner directly.",
	"Worthy Sacrifice": "A card bearing this sigil is counted as 3 blood rather than 1 blood when sacrificed.",
	"Custom": "TEST SIGIL"
}
...
```

This need to be done every time you add a new sigil so the game can know to load the sigil. When you are done with this you can then launch the game using the `Play` button on the top right or using `f5`.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/93a73093-75fc-4767-9ff4-8e3e9c6d6c4a)

When in the game switch to your ruleset (should be name `TEST`), make a new deck with your card in it and you can use the test feature of the deck editor, take note which window is there before the game open another window or full screen the game then use the test feature this make sure the console work correctly, for the purpose of the guide the main window (the one **you** open) will be call the **local window** and the second window (the one **the game** open) will be call the **remote window**.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/955e493c-4889-4572-8bd1-3ca5c72b86ec)

Here the big window is the local window you can know by looking at which player is which, `DEBUG_HOST` is the local window and `DEBUG_CLIENT` is the remote window

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/f46b6413-1521-43cd-be2b-2d95171e16f4)

After playing the card in the local window you should see it in the console that say `Custom`. Congratulation you have coded a simple sigil we will add functionality to it in the next section.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/6beee70f-8678-477f-b35b-12200c3f58c8)

## Testing Sigil (alternate)

> [!NOTE]
> This section is for the alternate method of making sigil, if you are using the game engine method skip this section.

After creating your sigil file make a new ruleset by going to the game directory go into `ruleset` and make a new file call `test.json` in this file put the following:

```json
{
	"ruleset": "TEST",
	"hammers_per_turn": 1,
	"ant_limit": 100,
	"deck_size_min": 1,
	"max_commons_main": 4,
	"max_commons_side": 10,
	"num_candles": 3,
	"variable_attack_nerf": false,
	"allow_snuffing_candles": true,
	"opt_actives": false,
	"enable_backrow": false,
	"starting_bones": 100000,
	"stating_energy_max": 100000,
	"portrait": "portraits/Stoat",
	"description": "TEST TIME",
	"cards": [
		{
			"name": "Thick",
			"attack": 0,
			"health": 2,
			"sigils": ["Custom"]
		},
		{
			"name": "Squirrel",
			"attack": 0,
			"health": 1
		}
	],
	"side_decks": {
		"10 Squirrels": {
			"type": "single",
			"card": "Squirrel",
			"count": 10
		}
	}
	"sigil_urls": {
		"Custom": "https://raw.githubusercontent.com/Mouthless-Stoat/sigil101/main/3-rabbit/Ant%20Hill.png"
	}
	"custom_sigils": {
		"Custom": {
			"description": "TEST",
		}
	}
}
```

What to take not is the last 2 field `sigil_urls` and `custom_sigils`. `sigil_url` let you download a portrait for the sigil but if it doesn't work you can download it [here](https://raw.githubusercontent.com/Mouthless-Stoat/sigil101/main/3-rabbit/Ant%20Hill.png) and putting it in the `custom_sigil_icon` folder in the game directory. `custom_sigils` is where you define custom sigil and tell the game to load them when creating card.

Now launch the game select your ruleset and start a test fight take note of which window the game opened and which one you start out with, the main window (the one **you** open) will be call the local window, the second window (the one **the game** open) will be call the remote window.

Here the big window is the local window you can know by looking at which player is which, `DEBUG_HOST` is the local window and `DEBUG_CLIENT` is the remote window

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/f46b6413-1521-43cd-be2b-2d95171e16f4)

After playing your card on the remote window surrender then quit and close the games, now go to the game folder and look in the `logs` folder and open the newest log (should be `godot.log`) look at the very bottom and hopefully you can see the `Custom Activated` message. You will have to redo this process every time you log or print something by closing the game go to `logs` and check the file. This is the downside of using this method of making sigils.

![image](https://github.com/Mouthless-Stoat/sigil101/assets/89868169/1454ca42-399b-487e-abe3-c23de4c8f4c1)
