# Jane Street Interview Question from SWE mock interview video
source: https://www.janestreet.com/mock-interview/

1. I have used dictionary-based implementation instead of tuples for one distinctive reason: the data is indexed in dictionary can be called by its key and value pair.
2. tuples are immutable.This means they cannot be modified after declaration which espcially useful in fact based situation.
3. However,the issue can be defused with simple code of  ``` copy_dict = dict.copy() ``` where the main dictionary implementation remains untouched from deletions and modifications.

#### note: Thank you to  Ms. Grace and Mr Nolen for providing a glimpse at Jane Street's interview process.

I  viewed the problem statement and intentionally avoided the provided solution so that I could attempt the problem independently and simulate an authentic interview experience.
