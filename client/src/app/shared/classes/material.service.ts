import { ElementRef } from "@angular/core"

declare var M:any //: { toast: (arg0: { html: string }) => void }

export interface MaterialInstance{
    open?():void
    close?():void
    destroy?():void
}

export class MaterialService{
    static toast(message:string){
        M.toast({html:message})
    }

    static initializeFloatingButton(ref:ElementRef){
        M.FloatingActionButton.init(ref.nativeElement)
    }

    static updateTextInputs(){
        M.updateTextFields()
    }

    static initModal(ref:ElementRef){
       return M.Modal.init(ref.nativeElement)
    }
}