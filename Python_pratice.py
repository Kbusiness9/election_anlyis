{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Thank You\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(type(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print(type(\"Drew\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "ballots = 1341\n",
    "print(type(ballots))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "ballots =1341\n",
    "print(type(73.81))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "ballots =1341\n",
    "print(type(\"\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "isDog = True\n",
    "print(type(isDog))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "True\n",
      "Diane\n",
      "73.81\n"
     ]
    }
   ],
   "source": [
    "num_candidates = 3\n",
    "winning_percentage = 73.81\n",
    "candidate = \"Diane\"\n",
    "won_election = True\n",
    "print(num_candidates)\n",
    "print(won_election)\n",
    "print(candidate)\n",
    "print(winning_percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n",
      "-2\n",
      "48\n",
      "20.5\n",
      "2\n",
      "14.5\n"
     ]
    }
   ],
   "source": [
    "print(5 + 2 * 3)\n",
    "print(8 // 5 - 3)\n",
    "print(8 + 22 * 2 - 4)\n",
    "print(16- 3 / 2 + 7 - 1)\n",
    "print(3 ** 3 % 5)\n",
    "print(5 + 9 * 3 / 2 - 4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "21\n",
      "-2\n",
      "-36\n",
      "14.666666666666666\n",
      "27\n",
      "14.5\n"
     ]
    }
   ],
   "source": [
    "print((5 + 2) * 3)\n",
    "print((8 // 5) - 3)\n",
    "print(8 + (22 * (2 - 4)))\n",
    "print(16 - 3 / (2 + 7) - 1)\n",
    "print(3 ** (3 % 5))\n",
    "print(5 + (9 * 3 / 2 - 4)) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "counties = [\"Arapahoe\",\"Denver\",\"Jefferson\"]\n",
    "print(counties)\n",
    "print(counties[0])\n",
    "print(counties[1])\n",
    "print(counties[2])\n",
    "print(counties[-1])\n",
    "print(counties[-2])\n",
    "print(counties[-3])\n",
    "\n",
    "print(\"----------\")\n",
    "print(len(counties))\n",
    "\n",
    "print(\"-------\")\n",
    "print(counties[0:2])\n",
    "print(counties[0:1])\n",
    "print(counties[:2])\n",
    "print(counties[1:])\n",
    "print(counties[1:3])\n",
    "print(\"--------\")\n",
    "\n",
    "\n",
    "counties.append(\"El Paso\")\n",
    "counties.insert(2, \"El Paso\")\n",
    "print(len(counties))\n",
    "print(counties)\n",
    "\n",
    "counties.remove(\"El Paso\")\n",
    "print(counties)\n",
    "\n",
    "counties.pop(3)\n",
    "#counties.pop(-1)\n",
    "print(counties)\n",
    "\n",
    "\n",
    "print(\"-------Update------\")\n",
    "counties[2] = \"El Paso\"\n",
    "print(counties)\n",
    "print(\"-----------\")\n",
    "\n",
    "\n",
    "counties = [\"Arapahoe\", \"Denver\", \"Jefferson\"]\n",
    "counties.append(\"El Paso\")\n",
    "counties.remove(\"Arapahoe\")\n",
    "counties.append(\"Denver\")\n",
    "counties.append(\"Jefferson\")\n",
    "counties.pop(0)\n",
    "counties.pop(0)\n",
    "counties.append(\"Arapahoe\")\n",
    "print(counties)\n",
    "\n",
    "print(\"----------\")\n",
    "counties_dict={}\n",
    "counties_dict[\"Arapahoe\"] = 422829\n",
    "counties_dict[\"Denver\"] = 463353\n",
    "counties_dict[\"Jefferson\"] = 432438\n",
    "\n",
    "print(counties_dict[\"Arapahoe\"])\n",
    "print(counties_dict[\"Denver\"])\n",
    "print(counties_dict[\"Jefferson\"])\n",
    "print(len(counties_dict))\n",
    "print(counties_dict.items())\n",
    "print(counties_dict.keys())\n",
    "print(counties_dict.values())\n",
    "print(counties_dict.get(\"Denver\"))\n",
    "print(\"-\"*30)\n",
    "voting_data = []\n",
    "voting_data.append({\"county\":\"Arapahoe\", \"registered_voters\": 422829})\n",
    "voting_data.append({\"county\":\"Denver\", \"registered_voters\": 463353})\n",
    "voting_data.append({\"county\":\"Jefferson\", \"registered_voters\": 432438})\n",
    "\n",
    "voting_data.append({\"county\": \"El Paso\", \"registered_voters\": 461149})\n",
    "voting_data.remove({\"county\":\"Arapahoe\", \"registered_voters\": 422829})\n",
    "voting_data.append({\"county\":\"Denver\", \"registered_voters\": 463353})\n",
    "voting_data.pop(0)\n",
    "voting_data.pop(0)\n",
    "voting_data.append({\"county\":\"Arapahoe\", \"registered_voters\": 422829})\n",
    "\n",
    "print(voting_data)\n",
    "\n",
    "\n",
    "# How many votes did you get?\n",
    "my_votes = int(input(\"How many votes did you get in the election? \"))\n",
    "#  Total votes in the election\n",
    "total_votes = int(input(\"What is the total votes in the election? \"))\n",
    "# Calculate the percentage of votes you received.\n",
    "percentage_votes = (my_votes / total_votes) * 100\n",
    "print(\"I received \" + str(percentage_votes)+\"% of the total votes.\")\n",
    "\n",
    "print(\"-\"*100)\n",
    "counties = [\"Arapahoe\",\"Denver\",\"Jefferson\"]\n",
    "if counties[1] == 'Denver':\n",
    "    print(counties[1])\n",
    "\n",
    "\n",
    "temperature = int(input(\"What is the temperature outside? \"))\n",
    "\n",
    "if temperature > 80:\n",
    "    print(\"Turn on the AC.\")\n",
    "else:\n",
    "    print(\"Open the windows.\")\n",
    "    \n",
    "\n",
    "   #What is the score?\n",
    "score = int(input(\"What is your test score? \"))\n",
    "\n",
    "# Determine the grade.\n",
    "if score >= 90:\n",
    "    print('Your grade is an A.')\n",
    "else:\n",
    "    if score >= 80:\n",
    "        print('Your grade is a B.')\n",
    "    else:\n",
    "        if score >= 70:\n",
    "            print('Your grade is a C.')\n",
    "        else:\n",
    "            if score >= 60:\n",
    "                print('Your grade is a D.')\n",
    "            else:\n",
    "                print('Your grade is an F.') \n",
    "    \n",
    "\n",
    "# What is the score?\n",
    "score = int(input(\"What is your test score? \"))\n",
    "\n",
    "# Determine the grade.\n",
    "if score >= 90:\n",
    "    print('Your grade is an A.')\n",
    "elif score >= 80:\n",
    "    print('Your grade is a B.')\n",
    "elif score >= 70:\n",
    "    print('Your grade is a C.')\n",
    "elif score >= 60:\n",
    "    print('Your grade is a D.')\n",
    "else:\n",
    "    print('Your grade is an F.')\n",
    "\n",
    "\n",
    "counties = [\"Arapahoe\",\"Denver\",\"Jefferson\"]\n",
    "if \"El Paso\" in counties:\n",
    "    print(\"El Paso is in the list of counties.\")\n",
    "else:\n",
    "    print(\"El Paso is not the list of counties.\")\n",
    "    \n",
    "    \n",
    "if \"Arapahoe\" in counties and \"El Paso\" in counties:\n",
    "    print(\"Arapahoe and El Paso are in the list of counties.\")\n",
    "else:\n",
    "    print(\"Arapahoe or El Paso is not in the list of counties.\") \n",
    "\n",
    "\n",
    "    \n",
    "x = 0\n",
    "while x <= 5:\n",
    "    print(x)\n",
    "    x = x + 1 \n",
    "\n",
    "    \n",
    "counties = [\"Arapahoe\", \"Denver\", \"Jefferson\"]\n",
    "\n",
    "for county in counties:\n",
    "    print(county)\n",
    "    \n",
    "numbers = [0, 1, 2, 3, 4]\n",
    "for num in numbers:\n",
    "    print(num)   \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
