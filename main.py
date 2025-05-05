import tkinter as tk
from tkinter import messagebox, scrolledtext

QUESTIONS = [
  """
  1. When driving in fog, you should:
  A. Use high-beam headlights.
  B. Use low-beam headlights.
  C. Drive with only parking lights on.
  D. Use emergency flashers only.
  """,

  """
  2. At a red traffic light, you may turn right:
  A. After you come to a complete stop and it is safe to do so.
  B. Without stopping if there is no oncoming traffic.
  C. Only if a sign permits you to do so.
  D. Only after letting one car go ahead of you.
  """,

  """
  3. When can you legally block an intersection?
  A. During rush hour traffic.
  B. Never.
  C. Only when you are turning left.
  D. If you entered on a green light.
  """,
  
  
  """
  4. If your vehicle starts to hydroplane, you should:
  A. Accelerate to regain traction.
  B. Slam on your brakes immediately.
  C. Take your foot off the accelerator.
  D. Turn your steering wheel sharply.
  """,
  
  
  """
  5. California’s “Basic Speed Law” says:
  A. You should always drive at the posted speed limit.
  B. You must never drive faster than is safe for current conditions.
  C. The maximum speed limit in California is 65 mph.
  D. You can drive 10 mph over the speed limit to keep up with traffic.
  """,
  
  
  """
  6. At a four-way stop, who has the right of way?
  A. The driver on the left.
  B. The driver who arrives last.
  C. The driver who arrives first.
  D. The driver who signals first.
  """,
  
  
  """
  7. If you are involved in a collision, you must exchange with the other person involved:
  A. Proof of insurance only.
  B. Driver’s license, vehicle registration, proof of insurance, and current address.
  C. Driver’s license and phone number only.
  D. Vehicle registration only.
  """,
  
  
  """
  8. A pedestrian with a white cane is:
  A. A senior citizen who must yield to vehicles.
  B. A person who is visually impaired.
  C. A person with a hearing disability.
  D. A street vendor selling goods.
  """,
  
  
  """
  9. Two sets of solid double yellow lines spaced two or more feet apart:
  A. May be crossed to enter or exit a driveway.
  B. Should be treated like a solid wall and not be crossed.
  C. Indicate a center left turn lane.
  D. Indicate an HOV lane.
  """,
  
  
  """
  10. When parking uphill on a two-way street with no curb, your front wheels should be:
  A. Turned to the left (toward the center of the road).
  B. Turned to the right (away from the road).
  C. Parallel with the pavement.
  D. It does not matter which way the wheels are pointed.
  """,
  
  
  """
  11. If you plan to pass another vehicle, you should:
  A. Assume they will let you over.
  B. Signal and pass when safe.
  C. Drive closely behind the car in front of you until you can pass.
  D. Flash your headlights to make the other driver slow down.
  """,
  
  
  """
  12. California law states that you must signal:
  A. For at least 50 feet before turning.
  B. Only when other cars are around.
  C. For at least 100 feet before turning or changing lanes.
  D. Only if you are turning right.
  """,
  
  
  """
  13. A green arrow at a traffic light means:
  A. Go straight only.
  B. You may proceed in the direction of the arrow if it is safe.
  C. Yield to pedestrians only.
  D. Stop, then proceed.
  """,
  
  
  """
  14. You are driving on a multi-lane freeway. The lane in the center is:
  A. The “fast” lane.
  B. The lane for slow-moving vehicles.
  C. The lane used for passing.
  D. The lane for smooth driving and through traffic.
  """,
  
  
  """
  15. In California, you must use your headlights:
  A. One hour before sunset.
  B. If you cannot see at least 1,000 feet ahead.
  C. 30 minutes after sunset to 30 minutes before sunrise.
  D. Only when it’s raining heavily.
  """,
  
  
  """
  16. When approaching a school zone with flashing yellow lights, you must:
  A. Maintain your speed.
  B. Stop immediately.
  C. Slow down to the posted school zone speed limit.
  D. Honk to alert children.
  """,
  
  
  """
  17. You should increase your following distance when:
  A. The roads are dry and clear.
  B. Driving behind a large vehicle that blocks your view.
  C. Traffic is light.
  D. You are in the far left lane.
  """,
  
  
  """
  18. When a traffic signal is not working at an intersection, you should:
  A. Treat the intersection as if it is a four-way stop.
  B. Proceed as if the light was green.
  C. Look for a police officer for instructions.
  D. Make a U-turn and avoid the intersection.
  """,
  
  
  """
  19. It is illegal for a person 21 years of age or older to drive with a blood alcohol concentration (BAC) of _______ or higher.
  A. 0.02%
  B. 0.06%
  C. 0.08%
  D. 0.10%
  """,
  
  
  """
  20. If you are under 21 years old, your BAC must be:
  A. 0.00%.
  B. 0.01% or higher.
  C. 0.05% to pass the driving test.
  D. No law applies to drivers under 21.
  """,
  
  
  """
  21. A solid yellow line next to a broken yellow line means:
  A. Passing is allowed in both directions.
  B. Passing is not allowed in either direction.
  C. Passing is allowed only on the side with the broken line.
  D. You can cross to turn left only.
  """,
  
  
  """
  22. When entering a freeway on an on-ramp, you should:
  A. Slow down to 25 mph, then merge.
  B. Stop on the ramp if there is no space to merge immediately.
  C. Accelerate to match the speed of traffic.
  D. Drive onto the freeway and then speed up.
  """,
  
  
  """
  23. You may cross a solid double yellow line:
  A. To pass another vehicle.
  B. To turn left into a private driveway.
  C. Under no circumstances.
  D. To make a U-turn in a business district.
  """,
  
  
  """
  24. A child under 2 years old must:
  A. Always be secured in a rear-facing child passenger restraint system unless the child weighs 40 or more pounds or is 40 or more inches tall.
  B. Sit in the front seat to see the road.
  C. Use only the regular seat belt.
  D. Be secured in a booster seat only.
  """,
  
  
  """
  25. When can you drive in a bike lane?
  A. Never.
  B. During rush hour.
  C. To make a right turn within 200 feet of the intersection.
  D. If the bike lane is empty.
  """,
  
  
  """
  26. When approaching an emergency vehicle that is stopped with its lights flashing, California’s “Move Over” law requires:
  A. Speeding up to pass the emergency vehicle.
  B. Driving in the far right lane as quickly as possible.
  C. Moving over one lane or slowing down if unable to change lanes safely.
  D. Honking to warn other drivers.
  """,
  
  
  """
  27. You arrive at an intersection with a green light. A pedestrian is in the crosswalk but crossing against the red signal. You should:
  A. Continue through because you have the green light.
  B. Honk to make them move faster.
  C. Stop and allow the pedestrian to finish crossing.
  D. Drive around the pedestrian.
  """,
  
  
  """
  28. Large trucks turning right onto a street with two lanes in each direction:
  A. Must stay in the right lane at all times.
  B. May need to swing wide to complete the turn.
  C. Are usually able to turn without crossing into the left lane.
  D. Can complete a turn faster than smaller vehicles.
  """,
  
  
  """
  29. When should you use your horn?
  A. To alert other drivers of danger.
  B. To express anger at slow drivers.
  C. Whenever you want to get someone’s attention for personal reasons.
  D. In heavy traffic to get cars to move faster.
  """,
  
  
  """
  30. If there is an oncoming car to your left and a bicyclist to your right, what is the best course of action?
  A. Drive closer to the bicyclist to avoid the oncoming car.
  B. Split the difference and drive exactly in the middle.
  C. Slow down and let the oncoming vehicle pass, then move to the left to allow more space for the bicyclist.
  D. Honk to make the bicyclist move off the road.
  """,
  
  
  """
  31. On a two-lane road where passing is unsafe, you drive behind a slow-moving vehicle. You should:
  A. Follow closely and try to pass in the same lane.
  B. Stay behind until you can safely pass.
  C. Pass on the shoulder.
  D. Honk until they move out of your way.
  """,
  
  
  """
  32. When driving at night, you should:
  A. Increase your following distance.
  B. Use your phone light to see the speedometer.
  C. Use only your parking lights in residential areas.
  D. Drive with your interior lights on.
  """,
  
  
  """
  33. If your car has airbags, you should:
  A. Sit as close to the steering wheel as possible.
  B. Place your hands behind the airbag panel.
  C. Move your seat so you are at least 10 inches from the airbag cover.
  D. Deactivate them unless driving on the freeway.
  """,
  
  
  """
  34. If your accelerator suddenly gets stuck and you cannot free it, you should:
  A. Turn off the engine immediately, even if you are moving.
  B. Shift to neutral, brake, and pull off the road.
  C. Pump the gas pedal quickly.
  D. Continue driving until you find a service station.
  """,
  
  
  """
  35. You are driving on the freeway behind a large truck. You should:
  A. Stay in the truck’s blind spot.
  B. Allow extra distance behind the truck.
  C. Drive close behind the truck to draft and save fuel.
  D. Assume the truck driver can see you.
  """,
  
  
  """
  36. The speed limit in a residential area is _____ unless otherwise posted.
  A. 15 mph
  B. 25 mph
  C. 35 mph
  D. 45 mph
  """,
  
  
  """
  37. When you see a yellow flashing traffic signal at an intersection, you should:
  A. Stop completely before entering the intersection.
  B. Treat it like a stop sign.
  C. Slow down and cross the intersection carefully.
  D. Quickly drive through before it turns red.
  """,
  
  
  """
  38. To turn left from a two-way street onto a one-way street, you should:
  A. Begin the turn with your left wheel as close as possible to the yellow dividing line.
  B. Start the turn in the right lane, then move to the left lane.
  C. Turn from any lane.
  D. Turn sharply and cut across the travel lanes.
  """,
  
  
  """
  39. U-turns in business districts are:
  A. Legal at all times.
  B. Illegal unless a sign permits them.
  C. Allowed only when there is no traffic around.
  D. Allowed in front of fire stations.
  """,
  
  
  """
  40. You must file a Report of Traffic Accident Occurring in California (SR 1) with the DMV within 10 days when:
  A. Your vehicle fails a smog test.
  B. You have an accident and there is an injury or death.
  C. You move to a new address.
  D. You sell your vehicle.
  """,
  
  
  """
  41. When parking downhill on a two-way street with a curb, you should:
  A. Turn your front wheels toward the curb.
  B. Turn your front wheels away from the curb.
  C. Leave your wheels straight.
  D. Place the gear in neutral only.
  """,
  
  
  """
  42. You are about to exit the freeway. When should you signal?
  A. About 5 seconds before exiting.
  B. About 2 seconds before exiting.
  C. Don’t signal if there’s no traffic behind you.
  D. Signal only if the exit is sharp.
  """,
  
  
  """
  43. You see a school bus ahead of you with flashing red lights. What must you do?
  A. Stop as long as the red lights are flashing.
  B. Drive slowly past the bus.
  C. Honk to let the driver know you are passing.
  D. Pass immediately before children exit.
  """,
  
  
  """
  44. The seat belt law in California states:
  A. Only the driver needs to wear a seat belt.
  B. Only passengers in the front seat need to wear seat belts.
  C. All occupants of a moving vehicle must wear seat belts.
  D. Seat belts are optional for adults.
  """,
  
  
  """
  45. If a driver is distracted, for example, by using a cell phone or eating, they are:
  A. Less likely to have an accident.
  B. More likely to miss critical objects on the road.
  C. Driving safely if they can multitask.
  D. Obeying the “hands-free” law correctly.
  """,
  
  
  """
  46. If a pedestrian is at a corner or crosswalk with no traffic lights, you should:
  A. Yield to the pedestrian, as they have the right of way.
  B. Go first if you are faster.
  C. Drive around them if there is room.
  D. Move over to the bike lane to go around them.
  """,
  
  
  """
  47. When approaching a roundabout, you should:
  A. Stop immediately before entering.
  B. Yield to traffic already in the roundabout.
  C. Always enter in the left lane.
  D. Pass large trucks in the roundabout.
  """,
  
  
  """
  48. When you change lanes or merge with traffic, you:
  A. Should first check mirrors, then check your blind spot.
  B. Only need to check your mirrors.
  C. Honk to alert other drivers.
  D. Rely solely on your rearview camera.
  """,

]

ANS = [
  "B",
  "A",
  "B",
  "C",
  "B",
  "C",
  "B",
  "B",
  "B",
  "B",
  "B",
  "C",
  "B",
  "D",
  "C",
  "C",
  "B",
  "A",
  "C",
  "A",
  "C",
  "C",
  "B",
  "A",
  "C",
  "C",
  "C",
  "B",
  "A",
  "C",
  "B",
  "A",
  "C",
  "B",
  "B",
  "B",
  "C",
  "A",
  "B",
  "B",
  "A",
  "A",
  "A",
  "C",
  "B",
  "A",
  "B",
  "A",
]

class QuizApp:
    def __init__(self, root, questions, answers):
        self.root = root
        self.root.title("California Driving Test")
        self.root.geometry("700x500")

        self.qas = list(zip(questions, answers))
        self.index = 0
        self.score = 0
        self.wrongs = []

        # UI elements
        self.question_box = scrolledtext.ScrolledText(root, width=85, height=10, wrap='word')
        self.question_box.pack(pady=20)
        self.question_box.config(state=tk.DISABLED)

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack()

        self.option_buttons = []
        for opt in ['A', 'B', 'C', 'D']:
            btn = tk.Button(self.btn_frame, text=opt, width=12,
                            command=lambda c=opt: self.check_answer(c))
            btn.pack(side='left', padx=10)
            self.option_buttons.append(btn)

        self.status = tk.Label(root, text="")
        self.status.pack(pady=10)

        self.load_question()

    def load_question(self):
        if self.index < len(self.qas):
            q_text, _ = self.qas[self.index]
            self.question_box.config(state=tk.NORMAL)
            self.question_box.delete('1.0', tk.END)
            self.question_box.insert(tk.END, q_text.strip())
            self.question_box.config(state=tk.DISABLED)
            self.status.config(text=f"Question {self.index + 1} of {len(self.qas)}")
        else:
            self.show_result()

    def check_answer(self, user_ans):
        q_text, correct_ans = self.qas[self.index]
        if user_ans.upper() == correct_ans:
            self.score += 1
        else:
            self.wrongs.append((q_text, correct_ans, user_ans))
        self.index += 1
        self.load_question()

    def show_result(self):
        result_msg = f"You got {self.score} out of {len(self.qas)} correct.\n"
        result_msg += "You passed!" if self.score >= 38 else "You failed."

        wrong_details = "\n\n".join([
            f"Q{idx+1}:\n{q.strip()}\nCorrect: {a}, Your Answer: {ua}"
            for idx, (q, a, ua) in enumerate(self.wrongs)
        ])

        messagebox.showinfo("Quiz Result", result_msg)
        if self.wrongs:
            wrong_window = tk.Toplevel(self.root)
            wrong_window.title("Incorrect Answers")
            txt = scrolledtext.ScrolledText(wrong_window, width=85, height=25, wrap='word')
            txt.pack()
            txt.insert(tk.END, wrong_details)
            txt.config(state=tk.DISABLED)

        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root, QUESTIONS, ANS)
    root.mainloop()
