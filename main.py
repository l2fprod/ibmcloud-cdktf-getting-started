#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput, TerraformVariable

from imports.ibm import ResourceGroup, IbmProvider

class MyStack(TerraformStack):
  def __init__(self, scope: Construct, ns: str):
    super().__init__(scope, ns)

    IbmProvider(self, "ibm")

    basename = TerraformVariable(self,
      "basename",
      type="string",
      default="cdktf-gs",
      description="Prefix to be used to name resources"
    )

    # define resources here
    group = ResourceGroup(self,
      'group',
      name=f"{basename.string_value}-group"
    )

    TerraformOutput(self,
      'group_id',
      value=group.id
    )

app = App()
MyStack(app, "ibmcloud-cdktf-getting-started")

app.synth()
