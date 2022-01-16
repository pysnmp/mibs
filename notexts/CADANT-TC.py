#
# PySNMP MIB module CADANT-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/CADANT-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 23:42:48 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
cadant, = mibBuilder.importSymbols("CADANT-PRODUCTS-MIB", "cadant")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Counter64, Bits, Counter32, Gauge32, IpAddress, iso, TimeTicks, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "Counter32", "Gauge32", "IpAddress", "iso", "TimeTicks", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cadTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4998, 0))
cadTextualConventions.setRevisions(('2009-10-15 00:00', '2009-09-14 00:00', '2009-08-28 00:00', '2008-10-23 00:00', '2008-08-06 00:00', '2007-11-05 00:00', '2007-06-25 00:00', '2006-10-16 00:00', '2006-08-23 00:00', '2006-07-27 00:00', '2006-07-27 00:00', '2005-12-02 00:00', '2005-08-30 00:00', '2005-09-23 00:00', '2005-08-31 00:00', '2004-11-12 00:00', '2004-09-15 00:00', '2004-03-09 00:00', '2003-12-18 00:00', '2003-08-20 00:00', '2003-06-08 00:00', '2003-05-08 00:00', '2003-04-21 00:00', '2003-04-04 00:00', '2003-04-01 00:00', '2003-03-31 00:00', '2003-03-17 00:00', '2002-11-01 00:00', '2002-10-25 00:00', '2002-10-16 00:00', '2002-09-25 00:00', '2001-02-03 00:00',))
if mibBuilder.loadTexts: cadTextualConventions.setLastUpdated('200910150000Z')
if mibBuilder.loadTexts: cadTextualConventions.setOrganization('Arris International Inc')
class ShelfId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99)

class CardId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99)

class CardSubId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 1)

class PortId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 99)

class CardType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 98, 99))
    namedValues = NamedValues(("dcard", 1), ("ecard", 2), ("fcard", 3), ("mcard", 4), ("rcard", 6), ("fanA", 7), ("fanB", 8), ("fanC", 9), ("fanD", 10), ("powerA", 11), ("powerB", 12), ("discdriveA", 13), ("discdriveB", 14), ("dmm", 15), ("unknown", 98), ("invalid", 99))

class CardSubType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 37, 40, 98, 99))
    namedValues = NamedValues(("dcardiu1d8u", 1), ("ecard4e", 2), ("fcard", 3), ("mcard", 4), ("rcard", 6), ("fanA", 7), ("fanB", 8), ("fanC", 9), ("fanD", 10), ("powerA", 11), ("powerB", 12), ("discdriveA", 13), ("discdriveB", 14), ("dcard1d8u", 20), ("dcard2d8u", 21), ("dcardiu2d8u", 22), ("dcardiu2d12u", 23), ("ecard8e", 30), ("ecard4oc3", 31), ("ecard7oc3", 32), ("ecard1oc12", 33), ("ecard1gig", 34), ("dcard0d12u", 35), ("dmm16m16p4iu", 36), ("dmm16m", 37), ("rcardhcp", 40), ("unknown", 98), ("invalid", 99))

class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99))
    namedValues = NamedValues(("dport", 1), ("uport", 2), ("eport10BaseT", 3), ("eport100BaseT", 4), ("macport", 5), ("mport", 6), ("eport1000BaseT", 7), ("uchannel", 8), ("eport10000BaseT", 9), ("dportMac", 10), ("invalid", 99))

class MacChlPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 8, 99))
    namedValues = NamedValues(("dport", 1), ("uchannel", 8), ("invalid", 99))

class PortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 99))
    namedValues = NamedValues(("autoNegotiate", 1), ("fullDuplex100Mpbs", 2), ("halfDuplex100Mpbs", 3), ("fullDuplex10Mpbs", 4), ("halfDuplex10Mpbs", 5), ("fullDuplex1000Mpbs", 6), ("halfDuplex1000Mpbs", 7), ("fullDuplex10000Mpbs", 8), ("invalid", 99))

class PortDetectedMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 98, 99))
    namedValues = NamedValues(("fullDuplex100Mpbs", 2), ("halfDuplex100Mpbs", 3), ("fullDuplex10Mpbs", 4), ("halfDuplex10Mpbs", 5), ("sfpFullDuplex1000BaseT", 9), ("sfpHalfDuplex1000BaseT", 10), ("sfpFullDuplex100BaseT", 11), ("sfpHalfDuplex100BaseT", 12), ("sfpFullDuplex10BaseT", 13), ("sfpHalfDuplex10BaseT", 14), ("sfpFullDuplex1000BaseSX", 15), ("sfpFullDuplex1000BaseLX", 16), ("sfpFullDuplex1000BaseLH", 17), ("sfpFullDuplex1000BaseLXLH", 18), ("sfpFullDuplex1000BaseZX", 19), ("sfpFullDuplex1000BaseCWDM", 20), ("sfpFullDuplex1000BaseDWDM", 21), ("xfpFullDuplex10GBaseSR", 22), ("xfpFullDuplex10GBaseLRM", 23), ("xfpFullDuplex10GBaseLR", 24), ("xfpFullDuplex10GBaseER", 25), ("xfpFullDuplex10GBaseZR", 26), ("xfpFullDuplex10GBaseLX4", 27), ("unknown", 98), ("invalid", 99))

class FlowControlMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 98, 99))
    namedValues = NamedValues(("on", 1), ("off", 2), ("desired", 3), ("unknown", 98), ("invalid", 99))

class AdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrimaryState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("is", 1), ("oos", 2))

class SecondaryState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notapplicable", 0), ("manual", 1), ("fault", 2), ("diagnostic", 3), ("overload", 4), ("normal", 5), ("degrade", 6), ("initializing", 7), ("swdownload", 8), ("firmwarepump", 9))

class UnknownState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("known", 0), ("unknown", 1))

class DuplexStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notapplicable", 0), ("active", 1), ("standby", 2), ("simplex", 3), ("protected", 4))

class MacPortId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 448)

class MacPortIdWithInvalid(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 449)

class EqActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notapplicable", 0), ("initialize", 1), ("switch", 2), ("remove", 3), ("restorecond", 4), ("restoreuncd", 5), ("systemreset", 6), ("cardreset", 7))

class OverloadStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("yellow", 2), ("red", 3))

class DiskVolumeUsageLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("minor", 2), ("major", 3), ("critical", 4))

class CadBridgeGroupId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(33, 255)

class CadBridgePortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("cm", 1), ("cpeauth", 2), ("cpeunauth", 3), ("any", 4), ("none", 5))

class VlanId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 1000000)

class FlowActivityState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("needy", 1), ("normal", 2), ("greedy", 3))

class InetAddressIPv4or6(TextualConvention, OctetString):
    reference = 'InetAddress from INET-ADDRESS-MIB, RFC2851'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ValueSizeConstraint(20, 20), )
class LineType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("console", 1), ("vty", 2))

class AAAmethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 5))
    namedValues = NamedValues(("none", 1), ("line", 2), ("local", 4), ("group", 5))

class SshService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("terminal", 1), ("sftp", 2))

class SshAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("password", 1), ("public-key", 2))

class SshCipher(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("other", 0), ("threedes", 1), ("arcfour", 2), ("blowfish", 3), ("cast", 4), ("aes", 5))

class SshCipherType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("threedes", 2), ("arcfour", 3), ("blowfish", 4), ("cast128", 5), ("aes128", 6), ("aes192", 7), ("aes256", 8), ("des", 9), ("rc4", 10))

class SshMacAlg(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("hmac-sha1", 2))

class SshProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ssh1", 1), ("ssh2", 2), ("ssh1ssh2", 3))

class CadDouble(TextualConvention, Counter64):
    status = 'current'
    displayHint = 'd-10'

class FirmwareSource(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("committed", 1), ("transient", 2), ("boot1", 3), ("boot2", 4), ("unknown", 5))

class PicType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 98, 99))
    namedValues = NamedValues(("cameven", 1), ("camevensp1to1", 2), ("camevensp2to1", 3), ("camevensp4to1", 4), ("camevensp8to1", 5), ("camodd", 6), ("camoddsp1to1", 7), ("camoddsp2to1", 8), ("camoddsp4to1", 9), ("camoddsp8to1", 10), ("camspare", 11), ("nam", 12), ("scm", 13), ("cam16d", 14), ("cam16dspare", 15), ("unknown", 98), ("invalid", 99))

class CadExtAclCondition(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("na", 0), ("eq", 1), ("ne", 2), ("lt", 3), ("le", 4), ("gt", 5), ("ge", 6), ("range", 7))

class ServerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("telnet", 1), ("ftp", 2), ("snmp", 3), ("syslog", 4), ("radius", 5), ("tacacs", 6), ("other", 7))

class AccountingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("start-stop", 1), ("stop-only", 2))

class CadIfDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("in", 1), ("out", 2))

class CadIpPort(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 65535), ValueRangeConstraint(-1, -1), )
class CadIpTos(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 254)

class CadIpTosMask(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 30), ValueRangeConstraint(224, 224), ValueRangeConstraint(254, 254), )
class CadProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 255), ValueRangeConstraint(-1, -1), )
class CadTcpFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("urg", 0), ("ack", 1), ("push", 2), ("rst", 3), ("syn", 4), ("fin", 5))

class CadAclType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("none", 0), ("std-access-list", 1), ("ext-access-list", 2), ("rate-limit-access-list", 3), ("remark", 4), ("ipv6-access-list", 5))

class CadAclString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class OUIAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class SchedWeekDay(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("sunday", 0), ("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6))

class SchedMonth(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("january", 0), ("february", 1), ("march", 2), ("april", 3), ("may", 4), ("june", 5), ("july", 6), ("august", 7), ("september", 8), ("october", 9), ("november", 10), ("december", 11))

class SchedDay(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("d1", 0), ("d2", 1), ("d3", 2), ("d4", 3), ("d5", 4), ("d6", 5), ("d7", 6), ("d8", 7), ("d9", 8), ("d10", 9), ("d11", 10), ("d12", 11), ("d13", 12), ("d14", 13), ("d15", 14), ("d16", 15), ("d17", 16), ("d18", 17), ("d19", 18), ("d20", 19), ("d21", 20), ("d22", 21), ("d23", 22), ("d24", 23), ("d25", 24), ("d26", 25), ("d27", 26), ("d28", 27), ("d29", 28), ("d30", 29), ("d31", 30), ("r1", 31), ("r2", 32), ("r3", 33), ("r4", 34), ("r5", 35), ("r6", 36), ("r7", 37), ("r8", 38), ("r9", 39), ("r10", 40), ("r11", 41), ("r12", 42), ("r13", 43), ("r14", 44), ("r15", 45), ("r16", 46), ("r17", 47), ("r18", 48), ("r19", 49), ("r20", 50), ("r21", 51), ("r22", 52), ("r23", 53), ("r24", 54), ("r25", 55), ("r26", 56), ("r27", 57), ("r28", 58), ("r29", 59), ("r30", 60), ("r31", 61))

class SchedHour(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("h0", 0), ("h1", 1), ("h2", 2), ("h3", 3), ("h4", 4), ("h5", 5), ("h6", 6), ("h7", 7), ("h8", 8), ("h9", 9), ("h10", 10), ("h11", 11), ("h12", 12), ("h13", 13), ("h14", 14), ("h15", 15), ("h16", 16), ("h17", 17), ("h18", 18), ("h19", 19), ("h20", 20), ("h21", 21), ("h22", 22), ("h23", 23))

class SchedMinute(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("m0", 0), ("m1", 1), ("m2", 2), ("m3", 3), ("m4", 4), ("m5", 5), ("m6", 6), ("m7", 7), ("m8", 8), ("m9", 9), ("m10", 10), ("m11", 11), ("m12", 12), ("m13", 13), ("m14", 14), ("m15", 15), ("m16", 16), ("m17", 17), ("m18", 18), ("m19", 19), ("m20", 20), ("m21", 21), ("m22", 22), ("m23", 23), ("m24", 24), ("m25", 25), ("m26", 26), ("m27", 27), ("m28", 28), ("m29", 29), ("m30", 30), ("m31", 31), ("m32", 32), ("m33", 33), ("m34", 34), ("m35", 35), ("m36", 36), ("m37", 37), ("m38", 38), ("m39", 39), ("m40", 40), ("m41", 41), ("m42", 42), ("m43", 43), ("m44", 44), ("m45", 45), ("m46", 46), ("m47", 47), ("m48", 48), ("m49", 49), ("m50", 50), ("m51", 51), ("m52", 52), ("m53", 53), ("m54", 54), ("m55", 55), ("m56", 56), ("m57", 57), ("m58", 58), ("m59", 59))

class CadCpeDeviceTypes(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cable-modem", 0), ("cpe", 1), ("ps", 2), ("mta", 3), ("stb", 4), ("tea", 5), ("erouter", 6), ("dva", 7), ("sg", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("reserved29", 29), ("reserved30", 30), ("reserved31", 31))

mibBuilder.exportSymbols("CADANT-TC", SchedDay=SchedDay, CadIpPort=CadIpPort, CadDouble=CadDouble, SshService=SshService, PicType=PicType, CardSubId=CardSubId, PortId=PortId, ShelfId=ShelfId, FirmwareSource=FirmwareSource, PrimaryState=PrimaryState, CadCpeDeviceTypes=CadCpeDeviceTypes, PYSNMP_MODULE_ID=cadTextualConventions, CadIpTosMask=CadIpTosMask, FlowActivityState=FlowActivityState, OverloadStatus=OverloadStatus, SchedWeekDay=SchedWeekDay, VlanId=VlanId, CadIfDirection=CadIfDirection, SshMacAlg=SshMacAlg, InetAddressIPv4or6=InetAddressIPv4or6, SchedMonth=SchedMonth, PortType=PortType, SecondaryState=SecondaryState, AdminState=AdminState, MacPortIdWithInvalid=MacPortIdWithInvalid, EqActionType=EqActionType, CadIpTos=CadIpTos, SshCipher=SshCipher, CadAclType=CadAclType, DuplexStatus=DuplexStatus, UnknownState=UnknownState, CadTcpFlags=CadTcpFlags, MacPortId=MacPortId, ServerType=ServerType, CardId=CardId, CadExtAclCondition=CadExtAclCondition, PortMode=PortMode, OUIAddress=OUIAddress, DiskVolumeUsageLevel=DiskVolumeUsageLevel, cadTextualConventions=cadTextualConventions, CardType=CardType, MacChlPortType=MacChlPortType, SshProtocol=SshProtocol, LineType=LineType, SshCipherType=SshCipherType, SchedMinute=SchedMinute, CadBridgeGroupId=CadBridgeGroupId, CadBridgePortType=CadBridgePortType, SshAuthMethod=SshAuthMethod, AccountingType=AccountingType, FlowControlMode=FlowControlMode, CardSubType=CardSubType, CadProtocolType=CadProtocolType, AAAmethod=AAAmethod, SchedHour=SchedHour, PortDetectedMode=PortDetectedMode, CadAclString=CadAclString)
