Project Overview
Goal: To implement ordinary set operations(bit strings) and multiset operations (counts) on a shared universal set, then integrate Change Request.

Project Plan
ID--Task	------------------------------------------------------------- Owner	----------------- Status	---------------------------- Evidence
Phase 0: Setup				
0.1	Create repo, folder structure, README			                       Addie & Erich                [IN PROGRESS]
0.2	Create GitHub issues for each task below			
0.3	Define and document universe ordering			
Phase 1: Part 1 (Sets)				
1.1	Bit string/Boolean array representation of A and B (n ≥ 10)		   Erich                    [Complete]	                            [339051f]
1.2	Implement NOT(A)			                                           Erich                    [Complete]	                            [425eef2]
1.3	Implement union, intersection			                               Erich                    [Complete]	                            [425eef2]
1.4	Implement difference (A − B)			                               Erich                    [Complete]	                            [425eef2]
1.5	Implement symmetric difference as (A − B) ∪ (B − A)			         Erich                    [Complete]	                            [425eef2]
1.6	Display bit string and element-name listing for every result		 Erich                    [Complete]		                          [435a245]
Phase 2: Part 2 (Multisets)				
2.1	Multiplicity representation (list or dict of counts)			        Addie                      [COMPLETE]
2.2	Choose A and B with ≥ 2 elements of multiplicity > 1 each			    Addie                      [COMPLETE]                          [d6a5c55]  
2.3	Implement max (union) and min (intersection)			                Addie                      [COMPLETE]
2.4	Implement truncated difference (never below 0)			              Addie                      [COMPLETE]                          [b765c57]
2.5	Implement sum			                                                Addie                      [COMPLETE]                          [7ffc964]
2.6	Label all output as multiset operations			
Phase 3: Shared Code and Testing				
3.1	Factor shared validation and formatting into common module			
3.2	Write 2–3 representative test cases per part			                                           [TODO]
3.3	Write edge cases (see below)			                                                           [TODO]
3.4	Run tests and save output to a results file			                                             [TODO]
Phase 4: Week 2 Change Request				
4.1	Read Canvas announcement; record requirement in the plan			
4.2	Create issue(s) and a branch for the change			
4.3	Identify impact on existing code; refactor if needed			
4.4	Implement new functionality inside the existing repo			
4.5	Add tests for the new requirement			
4.6	Rerun all Part 1 and 2 tests (regression)			
4.7	Merge via pull request			
Phase 5: Report and Submission				
5.1	Write report: design, test results, ordering			
5.2	Document Change Request impact with Git evidence			
5.3	Final check: all tasks have evidence, repo link works

------------------Schedule for project---------------------
Week 1 Phases 0 to 3: Parts 1 and 2 working and tested
Week 2 Phase 4: Change request announced, integrate, regression test
Final week: Phase 5: Report and evidence check
