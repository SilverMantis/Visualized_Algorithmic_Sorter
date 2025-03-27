import random
import tkinter as tk
from tkinter import Toplevel


# test array for testing sorting algorithms

# test_array = [10,20,30,10,20,30]
test_array = [random.randint(1,30),random.randint(1,30),random.randint(1,30),random.randint(1,30),random.randint(1,30),random.randint(1,30)]

print("Unsorted Array:                     ", test_array)


class VisSortApp:

    def __init__(self,array):
        # assigning and creating base configurations for main app
        self.array = array
        self.sorter = tk.Tk()
        self.sorter.title("Visual Sorter App")
        self.sorter.geometry("913x550")
        self.sorter.config(background="black")

        # creating values later to be used in algorithms and visualization functions
        self.paused = False
        self.array_sorted = False
        self.sorting = False
        self.info_shown = False
        self.choice_being_made = False
        self.info_col = "yellow"
        self.comp_counter = 0
        self.current_action = "Currently on standby"


        # values explaining each used algorithm, used within the algorithmic dictionary feature
        self.current_info = "None"

        self.insertion_info = "Insertion sort:\n\nloops over array by making elements (starting from second) anchor elements, then compares said anchor element, if previous element higher - moves anchor element back until previous element is not higher, if previous not higher - continues loop and makes next value new anchor"
        self.bubble_info = "Bubble sort:\n\ndouble loops over array length of array amount of times and compares selected 2 elements, if previous element higher - swaps higher element forwards then continues loop, if previous element not higher - continues loop and checks following elements"
        self.selection_info = "Selection sort:\n\nloops over array by setting elements as anchor points, checks anchor point against rest of list to find if lower/lowest value found, if lower/lowest value found - swapps anchor value with lower/lowest value, if not found - continue loop and set next value as anchor (in this case, the anchor value is the lowest value meaning all other values are higher and cannot be swapped with to sort)"
        self.merge_info = "Merge sort:\n\nRecursively splits up array until only singular values remaining, then compares all values and then according to comparison merges said values - lower values positioned on the left - repeatidly until array has been fully rejoined back into one array and sorted"


        # values representing original values of the used array
        self.orig_values = {
            0:array[0],
            1:array[1],
            2:array[2],
            3:array[3],
            4:array[4],
            5:array[5]
        }

        # values representing current values of used array
        self.values = {
            0:array[0],
            1:array[1],
            2:array[2],
            3:array[3],
            4:array[4],
            5:array[5]
        }

        # values representing current state/color of each value
        self.action_cols = {
            0: "white",
            1: "white",
            2: "white",
            3: "white",
            4: "white",
            5: "white"
        }

        
        # creating used text and buttons within app
        self.canvas = tk.Canvas(self.sorter, width=900, height=500,highlightbackground="black")
        self.canvas.grid(row=0,column=0,columnspan=5,sticky=tk.W+tk.E,padx=5,pady=5)

        self.button1 = tk.Button(self.sorter,text="Insertion Sort",command=self.sort,bg="#03c04a",activebackground="lightgreen")
        self.button1.grid(row=1,column=0,sticky=tk.W+tk.E,padx=5,pady=5)

        self.button2 = tk.Button(self.sorter,text="Bubble Sort   ",command=self.bubble_sort,bg="#03c04a",activebackground="lightgreen")
        self.button2.grid(row=1,column=1,sticky=tk.W+tk.E,padx=5,pady=5)

        self.button3 = tk.Button(self.sorter,text="Selection Sort",command=self.selection_sort,bg="#03c04a",activebackground="lightgreen")
        self.button3.grid(row=1,column=4,sticky=tk.W+tk.E,padx=5,pady=5)

        self.button4 = tk.Button(self.sorter,text="Merge Sort",command=self.merge_sort,bg="#03c04a",activebackground="lightgreen")
        self.button4.grid(row=1,column=3,sticky=tk.W+tk.E,padx=5,pady=5)

        self.unsort_button = tk.Button(self.sorter,text="Unsort",command=self.unsort,bg="#ed2939",activebackground="#FFA500",width=7)
        self.unsort_button.grid(row=1,column=2,sticky=tk.W+tk.E,padx=5,pady=5)

        self.info_text = tk.Message(text=self.current_info,width=120)

        self.visualization()

        self.sorter.mainloop()

    def algorithm_dict_messagebox(self):
        # creating base configurations for top level info selection window
        msg_box = Toplevel(self.sorter)
        msg_box.title("Choose an Option")
        msg_box.geometry("300x215")
        msg_box.config(background="black")
        
        # creating label and buttons for informational choices
        label = tk.Label(msg_box, text="Select an option to get information about:", font=("Arial", 12),fg="white",bg="black")
        label.pack(pady=10)

        
        btn1 = tk.Button(msg_box, text="Insertion Sort", command=lambda: [self.show_info("Insertion"), msg_box.destroy()])
        btn1.pack(fill="x", padx=10, pady=5)
        
        btn2 = tk.Button(msg_box, text="Bubble Sort", command=lambda: [self.show_info("Bubble"), msg_box.destroy()])
        btn2.pack(fill="x", padx=10, pady=5)
        
        btn3 = tk.Button(msg_box, text="Selection Sort", command=lambda: [self.show_info("Selection"), msg_box.destroy()])
        btn3.pack(fill="x", padx=10, pady=5)
        
        btn4 = tk.Button(msg_box, text="Merge Sort", command=lambda: [self.show_info("Merge"), msg_box.destroy()])
        btn4.pack(fill="x", padx=10, pady=5)

        btn4 = tk.Button(msg_box, text="Back", command=lambda: [self.info_reset(),msg_box.destroy()])
        btn4.pack(padx=10, pady=5)
        
        
    
    def visualization(self):
        self.canvas.delete("all")

        # creating rectangles with custom size and text representing array values
        self.rec_1 = self.canvas.create_rectangle(40,435 - self.values[0] * 10,120,470,fill=self.action_cols[0],outline="black")
        self.canvas.create_text(80, 450, text=self.values[0], font=("Arial", 20), fill="black")

        self.rec_2 = self.canvas.create_rectangle(190,435 - self.values[1] * 10,270,470,fill=self.action_cols[1],outline="black")
        self.canvas.create_text(230, 450, text=self.values[1], font=("Arial", 20), fill="black")

        self.rec_3 = self.canvas.create_rectangle(340,435 - self.values[2] * 10,420,470,fill=self.action_cols[2],outline="black")
        self.canvas.create_text(380, 450, text=self.values[2], font=("Arial", 20), fill="black")

        self.rec_4 = self.canvas.create_rectangle(490,435 - self.values[3] * 10,570,470,fill=self.action_cols[3],outline="black")
        self.canvas.create_text(530, 450, text=self.values[3], font=("Arial", 20), fill="black")

        self.rec_5 = self.canvas.create_rectangle(640,435 - self.values[4] * 10,720,470,fill=self.action_cols[4],outline="black")
        self.canvas.create_text(680, 450, text=self.values[4], font=("Arial", 20), fill="black")

        self.rec_6 = self.canvas.create_rectangle(790,435 - self.values[5] * 10,870,470,fill=self.action_cols[5],outline="black")
        self.canvas.create_text(830, 450, text=self.values[5], font=("Arial", 20), fill="black")


        # section for creating color key
        self.key_border = self.canvas.create_rectangle(5,5,185,122,fill="white")


        self.yellow_key = self.canvas.create_rectangle(165,10,180,25,fill="yellow")
        self.yellow_text = self.canvas.create_text(92.5,16,text="Values being compared =")        

        self.blue_key = self.canvas.create_rectangle(165,34,180,49,fill="#007FFF")
        self.blue_text = self.canvas.create_text(88,40,text="Value used as anchor/key =")

        self.violet_key = self.canvas.create_rectangle(165,57,180,72,fill="#FA86C4")
        self.violet_text = self.canvas.create_text(84,64,text="Value split from main array =")

        self.orange_key = self.canvas.create_rectangle(165,80,180,95,fill="#FFA500")
        self.orange_text = self.canvas.create_text(90,87,text="Values merged/swapped =")

        self.green_key = self.canvas.create_rectangle(165,103,180,117,fill="#03c04a")
        self.green_text = self.canvas.create_text(98,109,text="Array has been sorted =")
        

        # section for creating algorithm dictionary/info shower
        self.info_button_border = self.canvas.create_rectangle(895,10,870,35,fill=self.info_col)

        self.info_button_text = self.canvas.create_text(883,22,text="i",font=("Aerial",15),width=1)


        # creating text showing current action  
        self.action_bg = self.canvas.create_rectangle(740,0,200,38,fill="black")

        self.action = self.canvas.create_text(468,20,text=self.current_action,font=("Arial", 15),fill="white")

        actionbbox = self.canvas.bbox(self.action)

        self.canvas.coords(self.action_bg, actionbbox[0] - 5, 0, actionbbox[2] + 5, actionbbox[3] + 5)

        self.canvas.tag_bind(self.info_button_border, "<Button-1>", lambda event: self.message_box_wrapper())


    def message_box_wrapper(self):
        # wrapper to check wether message box already active and to execute code for button changes
        if self.info_shown == False and self.choice_being_made == False:
            print("now showing info")
            self.info_col = "gray"
            self.algorithm_dict_messagebox()
            self.info_shown = not self.info_shown
            self.choice_being_made = not self.choice_being_made
        elif self.info_shown == True and self.choice_being_made == False:
            self.info_reset()
        self.visualization()

    def show_info(self,algorithm_chosen,event = None):
        # assigning defenitions to be shown if corresponding button pressed for info showcase
        match algorithm_chosen:
            case "Insertion":
                self.current_info = self.insertion_info
            case "Bubble":
                self.current_info = self.bubble_info
            case "Selection":
                self.current_info = self.selection_info
            case "Merge":
                self.current_info = self.merge_info
        
        # updating vizualisation and values used
        self.info_text.config(text=self.current_info)
        self.choice_being_made = not self.choice_being_made
        self.info_text.grid(row=0,column=6,padx=3,pady=10)
        self.sorter.geometry("1060x550")

        self.visualization()
    
    
    def unsort(self):
        # unsorting and resetting all values and states back to original if algorithm finished
        if self.sorting == False:

            for key in range(len(self.array)):
                self.array[key] = self.orig_values[key]
                self.values[key] = self.orig_values[key]
            self.action_cols = {k: "white" for k in self.action_cols}
            print("Unsorted Array:                     ", test_array)
            self.current_action = "Array has been reset and unsorted!"
            self.array_sorted = False
        self.visualization()

    def color_reset(self):
        # function to reset all colors, mostly used to reset colors after specified time
        self.action_cols = {k: "white" for k in self.action_cols}
        self.visualization()

    def info_reset(self):
        # function to reset all algorithm dictionary/information values
        self.info_text.grid_forget()
        print("no longer showing info")
        self.info_col = "yellow"
        self.sorter.geometry("913x550")
        self.info_shown = not self.info_shown
        self.choice_being_made = not self.choice_being_made
        self.visualization()

    def value_search(self):

        highest_value = max(self.array)
        lowest_value = min(self.array)
        
        print("\nhighest value :",highest_value)
        print("lowest value :",lowest_value)


        self.visualization()
    




    def bubble_sort(self):
        # starting bubble sort
        if self.array_sorted == False and self.sorting == False:
            self.sorting = True
            self.current_action = "Beginning Bubble Sort!"
            self.visualization()
            self.i = 0 # tracking outter loop
            self.j = 0 # tracking inner loop
            self.sorter.after(1000, lambda: self.bubble_main())
        else:
            self.current_action = "Unavaliable, sorting in process/sorted"
            self.visualization()


    def bubble_main(self):
        if self.i < len(self.array) - 1:  # outer loop condition
            if self.j < len(self.array) - self.i - 1:  # inner loop condition
                # updating visualization for compared vlaues
                self.current_action = f"Comparing value {self.array[self.j]} to {self.array[self.j + 1]}"
                self.action_cols[self.j] = "yellow"
                self.action_cols[self.j + 1] = "yellow"
                self.visualization()
                self.sorter.after(1000, lambda: self.bubble_check())
            else:
                # if inner loop finished, array has gone through one round of checks/swaps
                self.j = 0
                self.i += 1
                self.sorter.after(500, lambda: self.bubble_main())
        else:
            # if outer loop finished, array has been sorted
            self.array_sorted = True
            print("\nSorted array using Bubble Sort:     ", self.array)
            self.current_action = "Array has been sorted with the Bubble Sort algorithm!"
            self.action_cols = {k: "#03c04a" for k in self.action_cols}
            self.sorting = False
            self.visualization()

    def bubble_check(self):
        # checking adjacent elements
        if self.array[self.j] > self.array[self.j + 1]:
            # if left element higher, swap
            self.sorter.after(1000, lambda: self.bubble_shift())
        else:
            # if not, reset visualization and continue algorithm
            self.current_action = f"Previous value not higher, continuing"
            # continuing index
            self.j += 1
            self.action_cols = {k: "white" for k in self.action_cols}
            self.visualization()
            self.sorter.after(1000,lambda:self.bubble_main())

    def bubble_shift(self):
        # swapping values and resseting visualization
        self.action_cols = {k: "white" for k in self.action_cols}
        self.action_cols[self.j] = "#FFA500"
        self.action_cols[self.j+1] = "#FFA500"
        self.current_action = f"Previous value higher, switching"
        self.sorter.after(1000,lambda: self.color_reset())
        
        self.array[self.j], self.array[self.j + 1] = self.array[self.j + 1], self.array[self.j]

        self.values = {
            0:self.array[0],
            1:self.array[1],
            2:self.array[2],
            3:self.array[3],
            4:self.array[4],
            5:self.array[5]
        }
        self.visualization()

        # continuing index
        self.j += 1
        self.sorter.after(1000, lambda: self.bubble_main())





    def sort(self):
        # starting insertion sort
        if self.array_sorted == False and self.sorting == False:
            self.sorting = True
            self.current_action = "Beginning Insertion Sort!"
            self.visualization()
            self.sorter.after(1000, lambda: self.main(1))
        else:
            self.current_action = "Unavaliable, sorting in process/sorted"
            self.visualization()
        
        
    def main(self,i):
        # if fully looped through and loop finished, array has been sorted
        if i >= len(self.array):
            self.array_sorted = True
            print("\nSorted array using Insertion Sort:  ", self.array)
            self.current_action = "Array has been sorted with the Insertion Sort algorithm!"
            self.action_cols = {k: "#03c04a" for k in self.action_cols}
            self.sorting = False
            self.visualization()
        
        # if not looped through and loop unfinished, assign key as the i'th value and visualise it
        if i < len(self.array):
            self.current_action = f"The value {self.array[i]} is chosen as key"
            self.action_cols[i] = "#007FFF"
            self.visualization()
            key = self.array[i]
            j = i - 1
        try:
            self.sorter.after(1000, lambda: self.check(i, j, key))
        except IndexError:
            pass

    def check(self,i,j,key):
        self.current_action = f"Comparing key with previous value of {self.array[j]}"
        self.action_cols[j] = "yellow"
        self.visualization()
        # compare key with previous value
        if j >= 0 and self.array[j] > key:
            self.current_action = "Previous value higher, shifting back until previous lower or equal"
            self.sorter.after(1000, lambda: self.shift(i, j, key))
        # previous value not higher, skip and continue itterating through array 
        else:
            self.current_action = "Previous value not higher, continuing algorithm"
            self.array[j + 1] = key
            self.visualization()
            self.sorter.after(2000, lambda: self.main(i + 1))

        # resseting visualization
        self.values = {
            0:self.array[0],
            1:self.array[1],
            2:self.array[2],
            3:self.array[3],
            4:self.array[4],
            5:self.array[5]
        }
        self.visualization()
        self.action_cols = {k: "white" for k in self.action_cols}
            
    def shift(self,i,j,key):
        # while previous value higher, shift one back and check again
        self.current_action = "Previous value higher, shifting back until previous lower or equal"
        self.array[j],self.array[j + 1] = self.array[j + 1],self.array[j]
        j -= 1
        # resseting value and key visualisation
        self.action_cols = {k: "white" for k in self.action_cols}
        self.action_cols[j + 1] = "#007FFF"
        self.sorter.after(1000, lambda: self.check(i, j, key))





    def selection_sort(self):
        # starting selection sort
        if self.array_sorted == False and self.sorting == False:
            self.sorting = True
            self.current_action = "Beginning Selection Sort!"
            self.visualization()
            self.sorter.after(1000, lambda: self.selection_main())
        else:
            self.current_action = "Unavaliable, sorting in process/sorted"
            self.visualization()


    def selection_main(self, i = 0):
        if i >= len(self.array) - 1:
            # if fully looped through, array has been sorted
            self.array_sorted = True
            print("\nSorted array using Selection Sort:  ", self.array)
            self.current_action = "Array has been sorted with the Selection Sort algorithm!"
            self.action_cols = {k: "#03c04a" for k in self.action_cols}
            self.sorting = False
            self.visualization()

        # setting anchor point and visualising it
        if i < len(self.array) - 1:
            self.current_action = "Beggining selection sort!"
            self.current_action = f"Made {self.array[i]} the anchor point for sorting"
            self.action_cols[i] = "#007FFF"
            self.visualization()

        self.sorter.after(2000, self.find_minimum, i, i, self.array[i])

    def find_minimum(self, i, min_index, known_min, j=None):
        if j is None:
            j = i + 1

        # checking remaining elements for minimum
        if j < len(self.array):
            self.current_action = f"Comparing current minimum with {self.array[j]}"
            self.action_cols[j] = "yellow"
            if self.array[j] < known_min:
                known_min = self.array[j]
                min_index = j
            self.visualization()
            self.sorter.after(1000, self.find_minimum, i, min_index, known_min, j + 1)
            return

        # swapping the minimum value if needed
        self.action_cols = {k: "white" for k in self.action_cols}
        if min_index != i:
            # resseting comparison visualization and creating swap visualization
            self.action_cols[i] = "#FFA500"
            self.action_cols[min_index] = "#FFA500"
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
            self.current_action = f"Swapping with found smallest value ({self.array[i]})"
            self.visualization()
            self.sorter.after(2000, lambda: self.color_reset())
        # if no lesser value and index same, restart with next index
        elif min_index == i and self.array_sorted == False:
            self.current_action = f"No lesser values found"
            self.visualization()

        # updating visualization
        if self.array_sorted == False:
            self.values = {
                0:self.array[0],
                1:self.array[1],
                2:self.array[2],
                3:self.array[3],
                4:self.array[4],
                5:self.array[5]
            }

            self.visualization()
            self.sorter.after(2000, self.selection_main, i + 1)





    def merge_sort(self):
        # starting merge sort
        if self.array_sorted == False and self.sorting == False:
            self.sorting = True
            self.comp_counter = 0
            self.current_action = "Beginning Merge Sort!"
            self.visualization()
            self.sorter.after(1000, lambda: self.merge_main(0, len(self.array)))
        else:
            self.current_action = "Unavaliable, sorting in process/sorted"
            self.visualization()
    
    
    def merge_main(self, start, end):
        self.action_cols = {k: "white" for k in self.action_cols}
        if end - start <= 1:  # stopping recursion when singular element detected
            return

        midpoint = (start + end) // 2

        # visualizing value splits from main array
        for i in range(start, end):
            self.action_cols[i] = "#FA86C4"
        self.current_action = f"Splitting values {self.array[start:end]}"
        self.visualization()

        # recursively split left half
        self.sorter.after(2000, lambda: self.merge_main(start, midpoint))

        # recursively split right half
        self.sorter.after(4000, lambda: self.merge_main(midpoint, end))

        
        # beggining merging and comparison after both sides split
        self.sorter.after(9000, lambda: self.merge_comparison())

    def merge_comparison(self):
        self.action_cols = {k: "white" for k in self.action_cols}
        # tracking how many times values compared to pass proper merge values
        
        self.comp_counter += 1
        match self.comp_counter:
            case 1:
                start, midpoint, end = 1, 2, 3
            case 2:
                start, midpoint, end = 4, 5, 6

            case 3:
                start, midpoint, end = 0, 1, 3
            case 4:
                start, midpoint, end = 3, 4, 6

            case 5:
                start, midpoint, end = 0, 3, 6  

        left = self.array[start:midpoint]
        right = self.array[midpoint:end]

        # visualizing values being compared
        for i in range(start, end):
            self.action_cols[i] = "yellow"
        self.current_action = f"Comparing {left} to {right}"
        self.visualization()

        # moving onto merge
        self.sorter.after(10000, lambda: self.merge(start, midpoint, end))

    def merge(self, start, midpoint, end):
        self.action_cols = {k: "white" for k in self.action_cols}
        left = self.array[start:midpoint]
        right = self.array[midpoint:end]
        # tracking arrays and subarrays
        i = j = 0
        k = start

        self.current_action = f"Merging values {self.array[start:end]}"

        # checking left and right values in subarrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                self.array[k] = left[i]
                i += 1
            else:
                self.array[k] = right[j]
                j += 1
            k += 1

        # copying leftover elements
        while i < len(left):
            self.array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            self.array[k] = right[j]
            j += 1
            k += 1
        
        # visualizing merging within subarrays
        for i in range(start, end):
            self.action_cols[i] = "#FFA500"
        self.visualization()
        self.sorter.after(1500, lambda: self.color_reset())

        self.values = {i: self.array[i] for i in range(len(self.array))}

        self.visualization()

        # if array length reached, array has been sorted
        if end - start == len(self.array):
            self.sorter.after(2000, lambda: self.merge_sort_finished())
    
    def merge_sort_finished(self):
        # visualizing sorted array
        print("\nSorted array using Merge Sort:      ", self.array)
        self.current_action = "Array has been sorted with the Merge Sort algorithm!"
        self.action_cols = {k: "#03c04a" for k in self.action_cols}
        self.sorting = False
        self.array_sorted = True
        self.visualization()


# running code
searchsorter = VisSortApp(test_array)