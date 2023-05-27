import json
import sys
sys.path.append('quest-data-type')
from quest_node import quest_node
from quest_tree import quest_tree

def build_quest_tree_from_json(json_data):
    quest_tree_obj = quest_tree()

    # Parse JSON data
    quests = json_data.get("quests", [])

    # Create quest nodes and append them to the quest_tree
    for quest_data in quests:
        quest_name = quest_data.get("name")
        quest_tree_obj.append(quest_name)

        subquests_data = quest_data.get("subquests", [])
        for subquest_data in subquests_data:
            subquest_name = subquest_data.get("name")
            quest_tree_obj.set_subquest(quest_name, subquest_name)

    return quest_tree_obj


# Example usage
json_data = """
{
    "quests": [
      {
        "name": "Introduction to Algebra",
        "subquests": [
          {
            "name": "Variables and Expressions"
          },
          {
            "name": "Linear Equations and Inequalities"
          },
          {
            "name": "Algebraic Manipulation"
          }
        ]
      },
      {
        "name": "Elementary Functions",
        "subquests": [
          {
            "name": "Linear Functions"
          },
          {
            "name": "Quadratic Functions"
          },
          {
            "name": "Polynomial Functions"
          }
        ]
      }
    ]
}
"""

# Parse JSON data
json_obj = json.loads(json_data)

# Build quest tree from JSON
quest_tree_obj = build_quest_tree_from_json(json_obj)

# Traverse and print the quest tree
quest_tree_obj.traverse()
