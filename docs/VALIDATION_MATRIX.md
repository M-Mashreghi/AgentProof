# Validation Matrix

| Risk | Guard | Blocking |
|---|---|---:|
| prior run leaks solution | run isolation | Yes |
| hidden answer exposed | context validator | Yes |
| benchmark version mismatch | manifest check | Yes |
| grader failure counted as agent failure | outcome taxonomy | Yes |
| perturbation semantics invalid | invariant validator | Yes |
| fault silently invalidates task | fault validator | Yes |
| confidence channels mixed | typed schema | Yes |
| recovery gets gold answer | recovery input guard | Yes |
| stale pricing | pricing version | Warning/Protocol |
| unsafe real action | sandbox guard | Yes |
| aggregate hides safety | dimension-level reporting | Yes |
| test tuning | experiment registry | Yes |
