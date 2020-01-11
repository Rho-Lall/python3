This is a collection of .py files and notebooks I've put together as a PyTorce reference.
These notes are beginner level and start with the basics of deep learning (neural networks).
This readme file will walk you thru the setup process if you need it.



*********************************************************************************************************************************************************************************
PYTORCH SETUP FOR YOUR LAPTOP.
*********************************************************************************************************************************************************************************

[TLDR: Don't waste the next two days of your life trying to setup your own personal PC for Deep Learning. To do deep learning, you’ll need access to a computer with an NVIDIA GPU (unfortunately other brands of GPU are not fully supported by the main deep learning libraries). However, don’t buy one; in fact, even if you already have one, don’t use it just yet! Setting up a computer takes time and energy, and you want all your energy to focus on learning deep learning. You can rent a computer that already has everything you need preinstalled and ready to go. You can use Google CoLab for free. This guide will get you setup on Google Colab.]

Reference: FastAI Notebooks on Colab: fastai/course-v3

Getting Pytorch Installed:
After attempting import torch and failing I visited, https://pytorch.org/get-started/locally/
to get started.

Prepare for it to take a while. At least it did for me. Trying this at the local library probs wasn't the best idea.

Still waiting. 66%

78%

84%

Ok. Pytorch is installed. 

What the hell is CUDA? 

"To check if your GPU driver and CUDA is enabled and accessible by PyTorch, run the following commands to return whether or not the CUDA driver is enabled":

torch.cuda.is_available()

I get False. 

Do I need CUDA? I have a decent graphics card so... maybe.

I think this video is helpful: https://www.youtube.com/watch?v=vMZ7tK-RYYc
1. [0:21] Install Anaconda - done.
2. [0:36] Install Conda
    <sarcasm>Yeah! More installations</sarcasm>
    @ the Anaconda Prompt enter: conda update conda
    12% 
    15%
    This is going to be a while.

    Meanwhile: An Introduction to GPU Programming with CUDA
    https://www.youtube.com/watch?v=1cHx1baKqq0
    CUDA is an NVIDIA product. CUDA stands for Compute Unified Device Architecture.
    CUDA is a programing framwork that lets programmers harness GPU cores for computation.
    CUDA is an extension of C. PyTorch is built on top of CUDA's CuDNN architecture.


    I ran out of time and had to restart back at home. It looks like it was smart enough to pick up where i left off.

3. [0:51] Install Numba
    1. @ the Anaconda Prompt enter: conda install Numba
    This is just like the previous install.
    But alot faster.

4. [1:07] Install CUDA Toolkit
    1. @ the Anaconda Prompt enter: conda install cudatoolkit
    This is taking it's sweet time... and i'm taking the kids to school.
    That is all. Installation complete!!!

5. Testing
    @ the Anaconda Prompt enter:
        import torch
        torch.cuda.is_available()

        It's still False.

    My notebook test: Testing CUDA
        This seems to work.
        I'm not sold on this test. 
    
Finishing Up: An Introduction to GPU Programming with CUDA
    https://www.youtube.com/watch?v=1cHx1baKqq0
    [3:36] CUDA is an NVIDIA product. CUDA stands for Compute Unified Device Architecture.
        CUDA is a programing framwork that lets programmers harness GPU cores for computation.
        PyTorch is built on top of CUDA's CuDNN architecture. CUDA is an extension of C.
    [4:04] GPU Processing: Under The Hood
    [5:04] Excercise


...
After doing some Googling I've realized that my AMD Radeon is great, but useless. And I've waisted the last two days.
https://www.quora.com/Does-CUDA-work-on-AMD-GPUs

That is fustrating. But for my troubles I did find this MOOC FROM USF:
https://course.fast.ai/index.html

To do deep learning, you’ll need access to a computer with an NVIDIA GPU (unfortunately other brands of GPU are not fully supported by the main deep learning libraries). However, don’t buy one; in fact, even if you already have one, don’t use it just yet! Setting up a computer takes time and energy, and you want all your energy to focus on learning deep learning. You can use Google Colaboratory (colab) for free. It comes with everything you need installed.


*********************************************************************************************************************************************************************************
INTRO TO GOOGLE COLAB 
*********************************************************************************************************************************************************************************

Colaboratory (CoLab) is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud.
Colab Getting Started Guide: https://course.fast.ai/start_colab.html
Reference: Welcome_To_Colaboratory.ipynb

PYTORCH & FASTAI

[From FastAI] We teach how to train PyTorch models using the fastai library. These two pieces of software are deeply connected—you can’t become really proficient at using fastai if you don’t know PyTorch well, too. Therefore, you will often need to refer to the PyTorch docs. And you may also want to check out the PyTorch forums (which also happen to use Discourse).

Of course, to discuss fastai, you can use our forums, and be sure to look through the fastai docs too.

Don’t worry if you’re just starting out—little, if any, of those docs and forum threads will make any sense to you just now. But come back in a couple of weeks and you might be surprised by how useful you find them…


At this point, if you followed along you are setup to do deep learning with Pytorch on Colab. The rest of my notes will assume you are at this point.


