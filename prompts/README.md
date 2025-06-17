# Prompts description


## Correlation Event

A Correlation Event is defined through the following Python class, according to the format required by GoLLiE:

```python
class CorrelationEvent(Template):
  """A CorrelationEvent refers to any dynamics, state change or relationship within a context involving one or more entities. Such as discovering, accusing, loving, helping, killing,
  firing, finding, cheating, divorcing, reporting. 
  """
  mention: str
  """
  The text span that most clearly expresses the CorrelationEvent. Such as: "discover", "kill", "find", "love", "accuse", "love", "criticize", "discover", "fire", "cheat", "report"
  """
  entities: Dict[str, str] # Dictionary of CorrelationEvents in which the keys correspond to entities and values correspond to the role that entity has in the context of the CorrelationEvent. Such as: "Alex":"victim", "Claire": "police officer", "John":"man", "lawyer":"speaker"

  ```


  ## Case selection


We selected 39 cases
related to legal matters that had significant media
impact due to evidences of cultural biases, such as
religious, political, gender, racial and media biases. 
Note that we  prioritized recent cases, due to the significant developments in the legal system and shifts in public opinion regarding civil rights, discrimination, and biases, over the years. The cases are shown as follows: 


| Subject                                 | Subject                              |
|-----------------------------------------|--------------------------------------|
| Britney Spears Conservatorship          | Troy Davis                           |
| Bill Cosby women accusation             | Ahmaud Arbery                        |
| Johnny Depp and Amber Heard             | Sandra Bland                         |
| Mike Ben Peter                          | Tamir Rice                           |
| Harvey Weinstein                        | Caster Semenya                       |
| Edward Snowden                          | Eluana Englaro                       |
| Breonna Taylor                          | Mohamed Wa Baile                     |
| Chelsea Manning                         | Kyle Rittenhouse                     |
| Rosemarie Aquilina                      | Starbucks Arrests                    |
| Trayvon Martin                          | Robert Kelly                         |
| Amanda Knox                             | Patrick Lyoya                        |
| Sarah Everard                           | Cyntoia Brown-Long                   |
| Youssef Nada                            | Dieudonné M'bala M'bala              |
| Dominique Strauss-Kahn                  | Nils Fiechter and Adrian Spahr       |
| Michael Brown                           | Philando Castile                     |
| Eric Garner                             | Ethan Couch                          |
| Terri Schiavo                           | Julian Assange political             |
| O.J. Simpson                            | Jussie Smollett                      |
| Johnny Depp and *The Sun*               | Ahmed Mohamed                        |
| Charlie Gard                            |                                      |


