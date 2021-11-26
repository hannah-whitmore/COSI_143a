# PA5- Entity Matching 
Due Friday May 7th, 11pm - NO LATE DAYS 

In this assignment you are give a  dataset that contains product data from Walmart and Amazon. The dataset contains two tables the left table (denoted by *ltable*), and the right table (denoted by *rtable*). Further, we are providing a dataset (*test.csv*) that contains a list of true product matches and no-matches for evaluation.

Table ltable has the following schema: ltable_id, title, category, brand, modelno, price

Table rtable has the following schema: rtable_id, title, category, brand, modelno, price

The testing data file has the following schema: ltable_id, rtable_id, label, id 

In the testing data file the label is 0 if the two products do not match and 1 if they match. 

*Helpful hint: to read the two tables you will need to use the encoding latin-1*

For this task you will need to solve the problem of entity matching over the provided records of products and then report the performance of your solution when evaluated on the testing dataset. 

You are expected to submit a notebook that implements the following:

1. Implement an entity matching solution between the two tables, using the Record linkage toolkit we introduced in class.
  + You can use any index you need as long as your notebook can be executed within a reasonable time frame. **Entity matching code that takes more than 5 mins to run will be getting zero points**. You can measure the time it takes for a cell to execute by using the command <code> %%time* </code> as the first line of your cell. 
  + *Hint* : A full index will take a long time to execute. You should be mindful of the number of product comparisons your code will execute. A blocked index on the other hand might miss some identical products if it looking for matches on the "wrong" set of attributes, if it is looking for exact strings vs similar strings, if the matching threshold is set to be too high, etc. You could use any of the indexing techniques we discussed in class or any others that you see fit based on the documentation of the [Record linkage toolkit](https://recordlinkage.readthedocs.io/en/latest/about.html) 
  
2. Report the final prediction for your matches in an output csv file that has the schema <ltable_id, rtable_id, prediction>. First line should have be this: ltable_id,rtable_id,prediction. Name your output file output.csv. 
  + Prediction should have the value 1 if the two products match and 0 otherwise. Include the output file in your submittion. 
  + How you decide the final prediction depends on the approach you used (and your intuition). For instance, if you are using 3 strings (title, category, brand) for your matching then you needs to decide if two products match if they agree on all or some of these 3 strings. 
  
3. Report the false positives and false negatives by comparing your matches with the ground truth (which is in the testing dataset test.csv we provided). You should also report the precision and recall of your solution and the F1 measure. 
  + We will also test the F1 measure of your matches. **The top-5 F1 measures in class will get 10 extra credit points**. This assignment is a competition!  Our solution got a 0.76 F1 measure but you could possibly do even better.  
  + Note: some of the product matches  (pairs of <ltable_id, rtable_id) > that appear in the test file we provided (the ground truth), might not appear in your  output of your and vice versa. We are asking you to evaluate the F1 measure in the intersection of those two sets. 
  
4. Describe in a markdown cell in your notebook the process you used for your solution. Why did you choose the specific index, why the specific attributes (if any) for your blocked index, why did you use or not the SortedNeighborhood algorithm for your index. We want to understand the process you used and we expect it to be  a bit more sophisticated  than  a random pick of parameters. In other words - defend your notebook! 

Good luck! 


## Grade 
The rubric below will be updated upon completion of grading 

<table>
  <thead>
    <tr>
      <th>Part</th>
      <th>Points</th>
      <th>Comments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Implementation (60 points)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>F-measure calculation  (25 points) </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td> Description  (15 points) </td>
      <td></td>
      <td></td>
    </tr>
     <tr>
      <td>Extra Credit  (10 points) </td>
      <td></td>
      <td></td>
    </tr>
     </tr>
  </tbody>
</table>
