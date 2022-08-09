#
# PySNMP MIB module MIMOSA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-MIB-TC
# Produced by pysmi-1.1.8 at Tue Aug  9 15:48:26 2022
# On host fv-az135-436 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
mimosa, = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosa")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, NotificationType, Unsigned32, IpAddress, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ModuleIdentity, Integer32, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ModuleIdentity", "Integer32", "ObjectIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mimosaMibTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356, 3))
mimosaMibTC.setRevisions(('2017-02-15 00:00',))
if mibBuilder.loadTexts: mimosaMibTC.setLastUpdated('201702150000Z')
if mibBuilder.loadTexts: mimosaMibTC.setOrganization('Mimosa Networks www.mimosa.co')
class DecimalOne(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class DecimalTwo(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class DecimalFive(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-5'

class Mimosa5GHzFrequency(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(4800, 6200)

class Mimosa5GHzChannelNumber(TextualConvention, Integer32):
    status = 'current'

mibBuilder.exportSymbols("MIMOSA-MIB-TC", DecimalOne=DecimalOne, PYSNMP_MODULE_ID=mimosaMibTC, Mimosa5GHzFrequency=Mimosa5GHzFrequency, DecimalTwo=DecimalTwo, DecimalFive=DecimalFive, mimosaMibTC=mimosaMibTC, Mimosa5GHzChannelNumber=Mimosa5GHzChannelNumber)
