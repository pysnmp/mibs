#
# PySNMP MIB module MIMOSA-MIB-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-MIB-TC
# Produced by pysmi-1.1.12 at Wed Oct  9 02:22:32 2024
# On host fv-az1144-128 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
mimosa, = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosa")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, MibIdentifier, ObjectIdentity, Bits, Counter32, Unsigned32, Counter64, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "MibIdentifier", "ObjectIdentity", "Bits", "Counter32", "Unsigned32", "Counter64", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mimosaMibTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356, 3))
mimosaMibTC.setRevisions(('2017-02-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mimosaMibTC.setRevisionsDescriptions(('First Revision of Textual Conventions defined for MIMOSA-MIB modules.',))
if mibBuilder.loadTexts: mimosaMibTC.setLastUpdated('201702150000Z')
if mibBuilder.loadTexts: mimosaMibTC.setOrganization('Mimosa Networks\n    \t\t\t  www.mimosa.co')
if mibBuilder.loadTexts: mimosaMibTC.setContactInfo('postal:\n    \tMimosa Networks, Inc.\n\t\t469 El Camino Real, Suite 100\n\t\tSanta Clara, CA 95050\n        email: support@mimosa.co')
if mibBuilder.loadTexts: mimosaMibTC.setDescription('Mimosa device MIB definitions')
class DecimalOne(TextualConvention, Integer32):
    description = 'Fixed point, one decimal'
    status = 'current'
    displayHint = 'd-1'

class DecimalTwo(TextualConvention, Integer32):
    description = 'Fixed point, two decimals'
    status = 'current'
    displayHint = 'd-2'

class DecimalFive(TextualConvention, Integer32):
    description = 'Fixed point, five decimals'
    status = 'current'
    displayHint = 'd-5'

class Mimosa5GHzFrequency(TextualConvention, Integer32):
    description = 'Represents the frequency in the range of 4800 to 6200'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(4800, 6200)

class Mimosa5GHzChannelNumber(TextualConvention, Integer32):
    description = 'Reprensents the channel Wifi ChannelWidth'
    status = 'current'

mibBuilder.exportSymbols("MIMOSA-MIB-TC", PYSNMP_MODULE_ID=mimosaMibTC, DecimalTwo=DecimalTwo, mimosaMibTC=mimosaMibTC, DecimalOne=DecimalOne, DecimalFive=DecimalFive, Mimosa5GHzChannelNumber=Mimosa5GHzChannelNumber, Mimosa5GHzFrequency=Mimosa5GHzFrequency)
