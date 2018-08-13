//
//  main.c
//  BinaryTree
//
//  Created by 姜明杰 on 17/10/2.
//  Copyright (c) 2017年 MINGJIE JIANG. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
struct Node{
    int val;
    struct Node *leftchild;
    struct Node *rightchild;
};

void search(struct Node *root, int v){
    if (root != NULL){
        if (root->val == v){
            printf("Find value!!\n");
        }else{
            if (v < root->val){
                search(root->leftchild, v);
            }else{
                search(root->rightchild, v);
            }
        }
    }else{
        printf("Sorry, can't find value");
    }
}
void insert(struct Node **tree, int v){
    if (*tree == NULL){
        *tree = (struct Node*)malloc(sizeof(struct Node));
        (*tree)->val = v;
    }else{
        if (v < (*tree)->val){
            insert(&(*tree)->leftchild,v);
        }else{
            insert(&(*tree)->rightchild,v);
        }
    }
}
void printTree(struct Node *root){
    if (root != NULL){
        printTree(root->leftchild);
        printf("%d\n",root->val);
        printTree(root->rightchild);
    }
}
struct Node* delete(struct Node *root, int v){
    struct Node *cur, *pre;
    cur = root;
    pre = root;
    int flag = -1;
    while(cur->val != v){
        if(v < cur->val){
            pre = cur;
            cur = cur->leftchild;
            flag = 0;
        }else{
            pre = cur;
            cur = cur->rightchild;
            flag = 1;
        }
    }
    if (flag == -1){
        if (cur->leftchild == NULL && cur->rightchild == NULL){
            free(root);
            return NULL;
        }
        if (cur->leftchild != NULL && cur->rightchild == NULL){
            cur = cur->leftchild;
            free(root);
            return cur;
        }
        if (cur->leftchild == NULL && cur->rightchild != NULL){
            cur = cur->rightchild;
            free(root);
            return cur;
        }
        else{
            cur = cur->leftchild;
            while(cur->rightchild != NULL){
                pre = cur;
                cur = cur->rightchild;
            }
            if (pre == root){
                root->val = cur->val;
                pre->leftchild = cur->leftchild;
                free(cur);
                return root;
            
            }else{
                if (cur->leftchild != NULL){
                    pre->rightchild = cur->leftchild;
                    root->val = cur->val;
                    free(cur);
                    return root;
                }else{
                    pre->rightchild = NULL;
                    root->val = cur->val;
                    free(cur);
                    return root;
                }
            }
        }
    }else{
        if (cur->leftchild == NULL && cur->rightchild == NULL){
            if(flag == 0){
                pre->leftchild = NULL;
            }else{
                pre->rightchild = NULL;
            }
            free(cur);
            return root;
        }
        if (cur->leftchild != NULL && cur->rightchild == NULL){
            if(flag == 0){
                pre->leftchild = cur->leftchild;
            }else{
                pre->rightchild = cur->leftchild;
            }
            free(cur);
            return root;
        }
        if (cur->leftchild == NULL && cur->rightchild != NULL){
            if(flag == 0){
                pre->leftchild = cur->rightchild;
            }else{
                pre->rightchild = cur->rightchild;
            }
            free(cur);
            return root;
        }
        else{
            struct Node *tmp;
            tmp = cur;
            pre = cur;
            cur = cur->leftchild;
            while(cur->rightchild != NULL){
                pre = cur;
                cur = cur->rightchild;
            }
            if (pre == tmp){
                tmp->val = cur->val;
                tmp->leftchild = cur->leftchild;
                free(cur);
                return root;
            }else{
                if (cur->leftchild != NULL){
                    pre->rightchild = cur->leftchild;
                    tmp->val = cur->val;
                    free(cur);
                    return root;
                }else{
                    pre->rightchild = NULL;
                    tmp->val = cur->val;
                    free(cur);
                    return root;
                }
            }
        }
    }
}
struct Node* buildTree(){
    struct Node *root = NULL;
    insert(&root,5);
    insert(&root,3);
    insert(&root,4);
    insert(&root,1);
    insert(&root,7);
    insert(&root,11);
    return root;
}
int main(int argc, const char * argv[]) {
    struct Node* root = buildTree();
    printTree(root);
    
}