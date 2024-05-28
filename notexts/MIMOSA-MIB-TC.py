#
# PySNMP MIB module MIMOSA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-MIB-TC
# Produced by pysmi-1.1.12 at Tue May 28 13:39:24 2024
# On host fv-az973-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
mimosa, = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosa")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Bits, Integer32, Counter64, TimeTicks, Unsigned32, Counter32, MibIdentifier, Gauge32, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Bits", "Integer32", "Counter64", "TimeTicks", "Unsigned32", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
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

mibBuilder.exportSymbols("MIMOSA-MIB-TC", Mimosa5GHzChannelNumber=Mimosa5GHzChannelNumber, Mimosa5GHzFrequency=Mimosa5GHzFrequency, PYSNMP_MODULE_ID=mimosaMibTC, DecimalOne=DecimalOne, DecimalFive=DecimalFive, mimosaMibTC=mimosaMibTC, DecimalTwo=DecimalTwo)
