#!/usr/bin/env python
# coding: utf-8

# In[1]:


A1="jagadish"
A2="aparna"
A3="ashu"
family=f"{A1.title()}"
print(family)


# In[3]:


family1=f"{A1.upper()} and {A2.upper()} are my parents"
print(family1,'\n',family)


# In[17]:


print('!!!my family tree!!!!'.upper(),'\njagadish'.upper(),'\taparna'.upper(), '\njayeeta'.title(),'\tsusmita'.title(),'\tashu'.title(),'\ndebjyoti','\tsamriddhi','\tdevansh','\ndipika')


# In[54]:


first=('ashutosh')
last=('banik')
nickname=('ashu')
name=('banik ashutosh')
fullname=f'{first.title()} {last.title()}'
full_name=f'my full name is {first.upper()} {last.upper()}'
nick_name=f'my nick name is {nickname.upper()}'
profession=f'I am a VFX artist'
full_name1=f'hi i am {name}'
full=["ashu","jaya","dodo"]
print(fullname,'\n',full_name,'\n','\t',nick_name.upper(),'\n', profession,'\n',full_name1.title())

print(full)
type(full)


# In[67]:


print('\n\tgrandfather'.upper())
print('              \n\t\t\t\tgrandmother'.lstrip())
print('\tfather'.title())
print('\t\tnmother')


# In[74]:


print("Ashutosh", '            \t\t\tBanik'.lstrip())

