# refresher on PCA and covariance matrix

# what to do?

Prepare a 10-minute teaching segment with slides on 

- 1-2 key concepts **covered in that notebook**.
- We want you to be able to demonstrate your ability to present an **engaging** presentation remotely
- Cover one topic comfortably


# Step 1: What does the module cover?

- What is a probe
- Why they matter
- 2. Training and comparing probes
- 3. Causal interventions
- 4. Probing for Deception
- 5. Attention Probes for High-Stakes Detection

# Step 2: Select 2 concepts that are engaging

- 2. Training and comparing probes
- 3. Causal Interventions

Note: removed the Attention probes for high-stakes. Most engaging is Causal Interventions ablating directions and steering.
You are actually doing shit to the model. Also, I do not have to learn one more thing before presentation.

# Step3: Do the modules

expected time: 2 hours

Track time on each

## extract_activations - 23 min
time: 23 min
hard: pytorch stuff
    - how tokenizer is invoked

## PCA

time: 31 min
hard: torch lib stuff -> need to practice torch libs
    - Math: eigenvalues, SVD and decompositions
    - Enroll in linalg2?
    - argsort
Takeaway:
    - unsupervised method shows samples are linearly separated in PCA space
    - Are linearly separated features in PCA space necesarily separated in orginal space?

## layer sweep: where does the truth live?

time: n/a
hard:
    - Not really
takeaway:
    - truth is represented after some computation is done (a couple of layers down), final layers typically lower performance as need to output token.

# step 4: Write down what was hard

# step 5: Activation patching

- Activation patching is when we add or remove a "concept vector" like a linear probe to a token position.
- The purpose of it is to establish if there is a causal link between the concept and the vector.
- Is the model using this information to make its next token prediction?