# automatically generated, do not modify

# namespace: 

import flatbuffers

class TransMsg(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsTransMsg(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TransMsg()
        x.Init(buf, n + offset)
        return x


    # TransMsg
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TransMsg
    def Type(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TransMsg
    def Content(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def TransMsgStart(builder): builder.StartObject(2)
def TransMsgAddType(builder, type): builder.PrependInt32Slot(0, type, 0)
def TransMsgAddContent(builder, content): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(content), 0)
def TransMsgEnd(builder): return builder.EndObject()
