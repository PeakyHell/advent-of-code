import re

def get_file_content(file_path):
    """
    Retrieve the content of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path, 'r') as f:
        return f.read()


def split_file(file_path):
    content = get_file_content(file_path)
    content = content.split("\n")

    rules = []
    updates = []

    for line in content:
        if re.match(r"\d{2}\|\d{2}", line):
            rules.append(line.split("|"))
        elif re.match(r"([0-9]+(,[0-9]+)+)", line):
            updates.append(line.split(","))
    return rules, updates


def update_includes_rule(update, rule):
    """
    Tells if an update contains the numbers of a rule.

    Args:
        update (list): The update to look in.
        rule (list): The rule containing the numbers to look for.

    Returns:
        boolean: Either the update contains the rule numbers or not
    """
    return rule[0] in update and rule[1] in update


def update_respects_rule(update, rule):
    """
    Tells if an update contains numbers in the order required by the rule.

    Args:
        update (list): The update to check.
        rule (list): The rule the update needs to respect.

    Returns:
        boolean: Either the rupdate respects the rule or not.
    """
    return update_includes_rule(update, rule) and update.index(rule[0]) < update.index(rule[1])


def rules_of_update(rules, update):
    """
    Retrieve the rules that the update must respect.

    Args:
        rules (list): The list of all the rules.
        update (list): The update we want the rules for.

    Returns:
        list: The list of the rules that the update needs to respect.
    """
    update_rules = []
    for rule in rules:
        if update_includes_rule(update, rule):
            update_rules.append(rule)
    return update_rules


def update_is_valid(update, rules):
    """
    Tells if an update is in the right order according to its rules.

    Args:
        update (list): The update to verify.
        rules (list): The list of all the rules.

    Returns:
        boolean: Either the update respects its rules or not
    """
    update_rules = rules_of_update(rules, update)
    for rule in update_rules:
        if not update_respects_rule(update, rule):
            return False
    return True


def middle_number_of_valid_update(update, rules):
    """
    Gets the middle number of the update if it's valid.

    Args:
        update (list): The update to verify and get the number from.
        rules (list): The list of all the rules.

    Returns:
        int: The middle number or 0 if the update is invalid.
    """
    return int(update[len(update)//2]) if update_is_valid(update, rules) else 0


def middle_nums_sum_of_valid_updates_in_file(file_path):
    rules, updates = split_file(file_path)
    sum = 0

    for update in updates:
        sum += middle_number_of_valid_update(update, rules)
    return sum

print(middle_nums_sum_of_valid_updates_in_file("./2024/day5/day5.txt"))