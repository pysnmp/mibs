#
# PySNMP MIB module MIMOSA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-MIB-TC
# Produced by pysmi-1.1.12 at Tue Sep 17 10:03:19 2024
# On host fv-az1427-100 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
mimosa, = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosa")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, Counter32, IpAddress, NotificationType, Counter64, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "Counter32", "IpAddress", "NotificationType", "Counter64", "iso", "ModuleIdentity", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("MIMOSA-MIB-TC", Mimosa5GHzChannelNumber=Mimosa5GHzChannelNumber, Mimosa5GHzFrequency=Mimosa5GHzFrequency, PYSNMP_MODULE_ID=mimosaMibTC, DecimalOne=DecimalOne, DecimalTwo=DecimalTwo, DecimalFive=DecimalFive, mimosaMibTC=mimosaMibTC)
