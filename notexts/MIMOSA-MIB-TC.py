#
# PySNMP MIB module MIMOSA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-MIB-TC
# Produced by pysmi-1.1.12 at Thu Apr  4 13:41:05 2024
# On host fv-az984-576 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
mimosa, = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosa")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, NotificationType, Unsigned32, Counter64, TimeTicks, Gauge32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Unsigned32", "Counter64", "TimeTicks", "Gauge32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "ModuleIdentity", "IpAddress")
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

mibBuilder.exportSymbols("MIMOSA-MIB-TC", PYSNMP_MODULE_ID=mimosaMibTC, mimosaMibTC=mimosaMibTC, DecimalFive=DecimalFive, DecimalOne=DecimalOne, Mimosa5GHzFrequency=Mimosa5GHzFrequency, Mimosa5GHzChannelNumber=Mimosa5GHzChannelNumber, DecimalTwo=DecimalTwo)
