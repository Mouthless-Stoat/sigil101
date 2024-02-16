# Chapter 3.2: Code hit the fan

## Drawing card

So as a `Rabbit Hole` clone we need to be able to draw card. Recall this is what our code look like:

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned":
		print("Custom Activated")
```

We can now add a few more lines to our body like this:

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned":
		print("Custom Activated")
		var card_to_draw = CardInfo.from_name("Squirrel") # get the card
		fightManager.draw_card(card_to_draw) # draw it
```

We added 2 new line to our body:

```gdscript
var card_to_draw = CardInfo.from_name("Squirrel") # get the card
fightManager.draw_card(card_to_draw) # draw it
```

Like the comment suggest the first line is getting the card we need to draw and the second draw that card. Now let decode what they mean, if you recall from Chapter 1 `CardInfo.from_name("Squirrel")` is a method call, this is using the game `CardInfo` which basically govern every card information/data, we use the method `from_name` like the name suggest to get a card data from name. The method `from_name` take in a string to use as the card name in this case the string and the card name is `"Squirrel"` so `from_name` will give us back the data of the `Squirrel` card. All you need to know for now is `CardInfo` is a special value that contain many method that can be use while dealing with card. You will meet more of these special value and this guide will call them namespace, they are part of the game custom sigil API to let us make sigils.

We then use the returned the card data and save it into a `card_to_draw` variable to then use later. Next we use another namespace `fightManager` and the method `draw_card` to draw the `Squirrel` card we just got. The `draw_card` take in a card data, construct the card and add it to the current player hand. We supply `draw_card` in this case with the `Squirrel` card data that we previously got and draw it into our hand. `fightManager` like the name suggest handle and manage the current fight, this namespace expose a few method that are useful to interact with the current fight.

Now we can test our sigil to see if it will draw our card or not. By launching the game, and we'll see that it does indeed draw us a card. But if you mess around with it some more you will find a few strange behaviour.

## Oh no the bugs

If you play a card on the local window we will see that the game sometime desync and we draw more card than we should have. This is apparent when we have 2 of our testing card in our hand, when we play one of them we will draw 2 cards. This is because when a event happen **all** card with the sigil will activate and run their corresponding code leading to unexpected behavior. This is a easy fix however recall that we have another parameter to our `handle_event` function, `params` like we know previously in Chapter 3.1:

> When a sigil activates the game call our `handle_event` function with the event name and some other parameter that we may want. `event` will be the event name that the sigil activate for and `params` will be the extra parameter.

One of these extra parameter is the card that activated the event, we can test for this if the current card that activated the event only then we can draw our squirrel. We can make this small adjustment to our code like so:

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned" and params[0] == card:
		print("Custom Activated")
		var card_to_draw = CardInfo.from_name("Squirrel") # get the card
		fightManager.draw_card(card_to_draw) # draw it
```

If we recall `params[0]` mean we are indexing an array in this case we are getting the first position of `params`, which is the card that activate the event. `card` is another special value unlike `fightManager` and `CardInfo`, `card` is a special variable that represent the current card that is running this function. We are checking if the card that activated the event (`param[0]`) is the same as (`==`) the current card (`card`) and if this happen and the event that was fire is `card_summoned` only then we will draw a squirrel.

Now if we test our sigil that bug of multiple drawing no longer happen. However when we play our card the opponent also draw a card which we may not want this also cause a desync and error. We can see this error when playing the card from the remote window.

Solving this issue is also very easy we just once again need to make a slight adjustment to our condition like so:

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned" and params[0] == card and isFriendly:
		print("Custom Activated")
		var card_to_draw = CardInfo.from_name("Squirrel") # get the card
		fightManager.draw_card(card_to_draw) # draw it
```

`isFriendly` is another special variable, that is a boolean and it check if the card being play right now is friendly (is played by that player) with the current client. This may sound complicated, but basically the game is multiplayer this mean each player have to handle their own sigil interaction instead of telling the host to handle everything which would be slow. Because both player handle sigil interaction we need to check if the client handling the interaction right now is friendly with the card. We don't need to handle the case where it is not our client so we won't implement that, but other sigil may need to consider this behavior that we will talk about in later chapter

Lastly if you want to you can replace the intermediate variable `card_to_draw` with the card fetch because we are not using it for anything else. We may also remove our print statement now that we know our sigil work correctly

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned" and params[0] == card and isFriendly:
		fightManager.draw_card(CardInfo.from_name("Squirrel")) # draw it
```

And you done it you coded a sigil and understand why everything is the way it is, we can compare our code to the actual in game implementation of `Rabbit Hole`:

```gdscript
extends SigilEffect

# This is called whenever something happens that might trigger a sigil, with 'event' representing what happened
func handle_event(event: String, params: Array):

	# attached_card_summoned represents the card bearing the sigil being summoned
	if event == "card_summoned" and params[0] == card and isFriendly:

		# Draw the rabbit
		fightManager.draw_card(CardInfo.from_name("Rabbit"))
```

We can see apart from the comment and the card name, our code is identical that mean we are on the right track.

## Stronger Squirrel

Instead of just giving a single boring squirrel let make a stronger one by changing it's attack and health.

```gdscript
extends SigilEffect

func handle_event(event: String, params: Array):
	if event == "card_summoned" and params[0] == card and isFriendly:
		var card_to_draw = CardInfo.from_name("Squirrel") # get the card

		# change stat
		card_to_draw.attack += 2
		card_to_draw.healt += 2

		fightManager.draw_card(card_to_draw) # draw it
```

First we revert back to having the `card_to_draw` variable this is to save the card data so we can modify it. The next 2 lines may look similar to method call but they are property access instead.

### Dictionary

Dictionary is another data type just like `Array` and `String`. Dictionary like the name imply is like a normal dictionary which have a word and a definition, in programming a dictionary is usually a list of key and value pair, the key is use to get the value just like how the word is use to find it definition in a normal dictionary. You can create a dictionary like so:

```gdscript
{
	"key1": "value1",
	"key2": "value2"
}
```

Key are are any other valid data type including variable like `int`, `float`, `String`, etc. And a value is also any valid data type. To make a new key you put the key then a `:` follow by the value, each key pair is separated by a `,`. Key must be unique that is they can not be in the same dictionary twice. To access a value in a dictionary using key we can use property access.

Property access look like method call because to some degree method call are property access. Like method call you can use dot notation which is `dict.key` to get any value back. There are alternative like `dict[key]` which also work, you would use this second method of accessing when your key is not a string like a `int`, `float`, etc.

```gdscript
var dict = {
	"hello": 1
	"world": 2
}

print(dict.hello) # 1
print(dict["hello"]) # 1
```

You can also assign value using property access follow from the previous example:

```
dict.hello = 10

print(dict.hello) # 10
```

---

Back to our sigil we are accessing the `attack` property of the card then using a new symbol `+=` to increase it. `+=` is a augmented assignment they they can be form using any binary operator and a `=`. Augmented assignment are shortcut way to write the following `x = x + 1` can be reduce to `x += 1` is similarly all the following are equivalent:

```gdscript
x *= 2 # x = x * 2
x **= 10 # x = x ** 10
x /= 3 # x= x / 3
```

However you cannot do `x &&= 10` or any other logical operator.

We are using this augmented assignment to increase the attack by `2`, `card_to_draw.attack += 2` is like writing `card_to_draw.attack += card_to_draw.attack + 2` but that is long so we will use the shortcut to write them. The next line follow a similar logic changing the card `health` instead of `attack`. You may have notice that these field are similar to the card data that go into the ruleset card in fact they are the same value, so any field you expect to exist on a card will also exist on the card data that `CardInfo.from_name` return.

## Sharing is Caring

Now that we created a sigil time to share it with other. To share sigil they need to edit a ruleset and add our sigil in. First send over your sigils file to your friend, you can find it in the game engine `FileSystem`. Right clickng on the `Custom.gd` file choose `Show in File Manager`, then send your friend this file and tell them to put it in the `scripts` folder in the game directory. Now pick your ruleset of choice and add this new fields to the bottom:

```json
{
...
    "sigil_urls": {
        "Custom": "https://raw.githubusercontent.com/Mouthless-Stoat/sigil101/main/3-rabbit/Ant%20Hill.png"
    }
    "custom_sigils": {
        "Custom": {
            "description": "Sigil description here",
        }
    }
...
}
```

And now give them this new ruleset. `sigil_url` is where the sigil portrait will be download like `pixport_url` for card and `custom_sigils` tell the game to load our sigil.

## Conclusion

We have written our first sigil, learn how to share it and the logic behind our sigil now go and make some sigil this is basically all you need to know look at other sigil code to take code from and try to understand them.
