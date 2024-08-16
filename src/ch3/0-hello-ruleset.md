# Hello ...Ruleset?

One final thing to learn before we start making our sigil is ruleset. This chapter will give you a basic understanding of ruleset, how they work and how to create a new ruleset. We will learn another language to create ruleset, `[] json`. `[] json` is a simple language to define card data and other info about the ruleset. Before you can make ruleset make, you need to know where to put them for the game to load:

1. Go into the game and choose the `[] Select Ruleset` option
2. You can choose to store your ruleset file somewhere else and simply choose `[] From File` when you need to load it or have it in a file and copy the text and choose `[] From JSON` instead.

> This is a long chapter because everything here is closely related but not long enough to be include as it own sub chapter so it is all here together. You might want to skip around so here is the table of content:
>
> -   [Basic of Json](#basic-of-json)
> -   [Basic of Ruleset](#basic-of-ruleset)
> -   [Card Objects](#card-objects)
> -   [Side Decks](#side-decks)
> -   [Custom Sigils](#custom-sigils)

## Basic of Json

`[] json` is the main language that ruleset are written in, it is not a very complicated language it can only carry hard-coded data and can't really do anything else. `[] json` are written similarly to `Dictionary`. Let look at a example `[] json` file:

@f test.json

```json
{
    "string": "TEST",
    "array": [1, 2, 3]
}
```

First, everything must be between `[] {}` and every key have to be a `String` unlike with `Dictionary`, other than that they are pretty similar. There is a few quirk with `[] json` thought, most notable is you can't have trailing or hanging commas and `[] json` does not have comments.

## Basic of Ruleset

Ruleset are relatively simple. Every ruleset must have a header portion where you state all the basic setting that tell the game how your ruleset work from how many candles you have to how active sigils function. To include a setting you simply specify the setting name and it's value. Here a example of what a normal header look like:

> We're gonna exclude the outer `[] {}` for simplicity sake. Every option listed below are **necessary** to include or strange things will happen.

```json
@@snip ./listings/3-1.json:header
```

@c Listing 3-1: An example ruleset.

We will separate the setting into 5 main group to more easily talk about them:

-   [Name](#name)
-   [Features](#features)
-   [Card](#card)
-   [Deck](#deck)
-   [Experimental](#experimental)

### Name

This group let you configure how you ruleset look in the selection screen.

```json
@@snip ./listings/3-1.json:name
```

-   `[] ruleset`: The name of the ruleset.
-   `[] portrait`: The portrait/icon to use for the ruleset.

    > The value of this setting is the path to your ruleset icon. The path will start from [`[] gfx`](https://github.com/107zxz/inscr-onln/tree/main/gfx) folder in the game files. For example if you give it the value `"portraits/Egg"` it will point to this file:
    >
    > ![image](https://raw.githubusercontent.com/107zxz/inscr-onln/main/gfx/portraits/Egg.png)

-   `[] description`: The description of the ruleset.

### Features

This group allow you to configure certain game feature.

```json
@@snip ./listings/3-1.json:features
```

-   `[] hammers_per_turn`: How many hammer are allowed per turn.
-   `[] num_candles`: How many candles each player have.
-   `[] allow_snuffing_candles`: If the players are allow to snuff their own candles for a `[] Greater Smoke`.
    > You must have a card called `[] Greater Smoke` for this option to work

### Card

This group allow you to configure or cards and some sigil behave.

```json
@@snip ./listings/3-1.json:cardopt
```

-   `[] ant_limit`: Ant card max attack before they stop increasing.
-   `[] variable_attack_nerf`: Make card with variable attack always deal 1 damage to face.
-   `[] opt_actives`: Make active sigils only useable once per turn.

### Deck

This group allow you to configure deck building options.

```json
@@snip ./listings/3-1.json:deck
```

-   `[] max_commons_main`: Amount of same name common cards are allow in a deck.
-   `[] max_commons_side`: Amount of same name common cards are allow in a side deck.
-   `[] deck_size_min`: Minimum length for a deck.

### Experimental

This group allow you to configure experimental features, that are not yet stable so you shouldn't really use them.

```json
@@snip ./listings/3-1.json:experimental
```

-   `[] enable_backrow`: enable the backrow.

## Card Objects

After defining all the header option you can move on to actual define every card in your ruleset. These go into an `Array` in the option `[] cards` like so. Each elements in this `Array` is a `Dictionary` correspond to the information about a card. The information follow a schema and so we will be calling them `[] Card Object`. Here a small example of a few cards:

```json
@@snip ./listings/3-1.json:cards
```

This above define 4 cards: `[] Squirrel`, `[] Wolf`, `[] Adder` and `[] Sigil Test`.

Every cards must follow these schema for the game to render them correctly:

> Only the first 3 options are required and everything else is optional. Negative cost are possible and it will act like a free card but give you the resource when played.

-   `[] name`: Name of the card.
-   `[] attack`: Attack/power value of the card.
-   `[] health`: Health value of the card.
-   `[] pixport_url`: The card custom portrait url.
    > You would usually host these card portrait on a site. Most member of the community host them on [GitHub](https://github.com). When hosting the image in GitHub you would first upload the file, then open it. For example like this [card](https://github.com/107zxz/inscr-onln-ruleset/blob/main/portraits/Floating%20Eye.png), next you would want to change the world `[] blob` in the url to `[] raw`, reload the page with that link and use that new link in this field.
-   `[] description`: Description of the card.
-   `[] blood_cost`: Blood cost of the card.
    > Negative blood have some strange behaviour. Negative blood is treated as a 1 blood when you are sacrificing card, but it will always bypass the available blood check.
-   `[] bone_cost`: Bone cost of the card.
-   `[] energy_cost`: Energy cost of the card.
-   `[] mox_cost`: Mox cost of the card.
    > This must be a `Array` of `"Orange"`, `"Green"` and `"Blue"`. Including a value more than once doesn't do anything
-   `[] sigils`: Sigils of the card.
    > If a card have a active sigil you can't have any other sigil or it won't render correctly.
-   `[] active`: Make the card sigils into active sigils.
    > You should only enable this option if you card have an active sigil. You can usually only have 1 active sigil.
-   `[] atkspecial`: Give the card variable attack power.
    > There are only a few possible value for this option:
    >
    > -   `"mox"`: Power from amount of Mox cards. Mox cards are define as containing the word `[] Mox` within the name.
    > -   `"green_mox"`: Power from amount of Green Mox cards. Green Mox cards are define as containing the sigil `[] Green Mox`
    > -   `"mirror"`: Power from the opposing card power.
    > -   `"ant"`: Power from amount of ant cards. Ant cards are define as containing the word `[] Ant` within the name. This can only go up to the `[] ant_limit` option in the header. The starting power is determine by the `[] attack` option.
-   `[] conduit`: Make the card conductive
-   `[] rare`: Make the card rare.
-   `[] banned`: Make the card undraftable in the main deck.
-   `[] nohammer`: Make the card unhammerable.
-   `[] nosac`: Make the card unsacable.
-   `[] song`: Song to play when playing the card.
-   `[] evolution`: Name of the card to turn into after transforming.
-   `[] left_half`: Name of the card left half after splitting.
-   `[] right_half`: Name of the card right half after splitting.
    > The last few option `[] song` `[] evolution`, `[] left_half`, `[] right_half` only function if you have their respective sigil:
    >
    > -   `[] song`: `[] Music Player`
    > -   `[] evolution`: `[] Fledgling`, `[] Frozen Away` or `[] Transformer`
    > -   `[] left_half`, `[] right_half`: `[] Thick`

## Side Decks

After the cards you can include side option. These will go into an `Dictionary` in the option `[] side_decks`. Each key will be the name of the side deck option and each value configure the side deck for that name:

```json
@@snip ./listings/3-1.json:sides
```

This option define 3 side deck options:

-   A normal fix option name `[] 10 Squirrel`, with 10 `[] Squirrel` in the side deck.
-   A draftable option named `[] Mox Draft`. That have a maximum of 10 cards and allow to draft `[] Ruby Mox`, `[] Emerald Mox` and `[] Sapphire Mox`.
-   A grouped option where you first choose it and choose a sub category.

Every value in the `Dictionary` must first have a `[] type` then what else to include is depend on which type you choose, below is every `[] type` and what else to include with that type:

-   `[] single`: A fix side deck fill with 1 type of card.
    -   `[] card`: The card to fill the side with.
    -   `[] count`: How many card to fill with.
-   `[] draft`
    -   `[] cards`: Possible cards to draft from.
    -   `[] count`: Maximum amount of card allowed.
-   `[] single_cat`: A group of `[] single` together under the same name.
    -   `[] cards`: A `Dictionary` of `[] single` to be the sub group.

## Custom Sigils

Lastly is the custom sigil declaration. These will again be a `Dictionary` in the option `[] custom_sigils`. Each key will be the custom sigil name and each value is the sigil configuration. Here a small example configuration:

```json
@@snip ./listings/3-1.json:sigils
```

This declare a custom sigils named `[] Chungus` with the description `[] Big` from the creator `[] 107zxz`.

The sigil configuration must follow this schema:

-   `[] description`: The description to display for this sigil.
-   `[] author`: The author or creator of this sigil.
-   `[] url`: The url on where the find the sigil file.
    > Like the `pixport_url` option, you would want to include the file on a site. The advice for `pixport_url` also apply here.
-   `[] icon_url`: The url of the sigil icon.
    > Same as other url mention here.
