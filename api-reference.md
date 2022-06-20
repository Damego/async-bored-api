# API Reference

## ActivityType

Represents activities types.

{% tabs %}
{% tab title="Attributes" %}
* EDUCATION = "education"&#x20;
* RECREATIONAL = "recreational"&#x20;
* SOCIAL = "social"&#x20;
* DIY = "diy"&#x20;
* CHARITY = "charity"&#x20;
* COOKING = "cooking"&#x20;
* RELAXATION = "relaxation"&#x20;
* MUSIC = "music"&#x20;
* BUSYWORK = "busywork"
{% endtab %}
{% endtabs %}

## BoredActivity

Represents responce of request

{% tabs %}
{% tab title="Attributes" %}
* activity: `Optional[str]`
* accessibility: `Optional[float]`
* type: `Optional[ActivityType]`
* participants: `Optional[int]`
* price: `Optional[float]`
* key: `Optional[int]`
* link: `Optional[str]`
* error: `Optional[str]`
{% endtab %}
{% endtabs %}

## BoredClient

Represent methods to send request to bored api

{% tabs %}
{% tab title="Methods" %}
### get()

Gets a event with given parameters or random event if parameters not given.

**Parameters:**&#x20;

* key: `Optional[int]` = None
* type: `Optional[Union[ActivityType, str]]` = None
* participants: `Optional[int]` = None
* price: `Optional[float]` = None
* min\_price: `Optional[float]` = None
* max\_price: `Optional[float]` = None
* accessibility: `Optional[float]` = None
* min\_accessibility: `Optional[float]` = None
* max\_accessibility: `Optional[float]` = None

**Returns** `BoredActivity`\


### get\_random()

Find a random activity. Similar as `get()` **** with no given parameters.

**Returns** `BoredActivity`\


### get\_by\_key()

Find an activity by its key.

**Parameters:**

* key: `int`

**Returns** `BoredActivity`\


### get\_by\_type()

Find a random activity with a given type.

**Parameters:**

* type: `Union[ActivityType, str]`

**Returns** `BoredActivity`\


### get\_by\_participants()

Find a random activity with a given number of participants.

**Parameters:**

* participants: `int`

**Returns** `BoredActivity`\


### get\_by\_price()

Find an activity with a specified price.

**Parameters:**

* price: `float`

**Returns** `BoredActivity`\


### get\_by\_min\_max\_price()

Find an event with a specified price in an inclusively constrained range.

**Parameters:**

* min\_price: `float`
* max\_price: `float`

**Returns** `BoredActivity`\


### get\_by\_accessibility()

Find a price in an inclusively constrained range.

**Parameters:**

* accessibility: `float`

**Returns** `BoredActivity`\


### get\_by\_min\_max\_accessibility()

Find an event with a specified accessibility in an inclusively constrained range.

**Parameters:**

* min\_accessibility: `float`
* max\_accessibility: `float`

**Returns** `BoredActivity`
{% endtab %}
{% endtabs %}

